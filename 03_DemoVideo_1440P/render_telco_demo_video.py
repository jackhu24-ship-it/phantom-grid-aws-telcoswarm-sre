 # -*- coding: utf-8 -*-
"""
PHANToM GRID // PG-MOD-TELCO-SRE :: Clean Teleprompter Video Engine (No Sub-Box)
Target: 03_DemoVideo_1440P/PHANTOM_GRID_AWS_Telco_Demo_1440P.mp4
Ratified by: COMMANDER JACK HU x SEC XIAOMI
Features: Cyan Sub-Box Removed, Golden Pointer Focus, 56pt Text, Exact Audio Sync.
"""

import os
import sys
import time
import math
import subprocess
from pathlib import Path

print("[*] SCRIPT TRIGGERED: Initializing Clean Teleprompter Video Engine...")
sys.stdout.flush()

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("[!] ERROR: Pillow is not installed. Please run: pip install pillow")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = Path(__file__).resolve().parent
OUTPUT_MP4 = OUTPUT_DIR / "PHANTOM_GRID_AWS_Telco_Demo_1440P.mp4"
TEMP_DIR = OUTPUT_DIR / "temp_render_frames"

WIDTH = 2560
HEIGHT = 1440

ACTS = [
    {
        "act_id": "ACT 1: MISSION PROFILE & AWS CDS EVENT INGRESS",
        "sentences": [
            {
                "text": "Welcome to PHANToM Grid TelcoSwarm SRE reliability engine.",
                "voice": "Welcome to Phantom Grid Telco Swarm S, R, E reliability engine."
            },
            {
                "text": "Transient network degradation causes severe nine thousand dollar SLA penalties.",
                "voice": "Transient network degradation causes severe nine thousand dollar SLA penalties per minute."
            },
            {
                "text": "Our autonomous agent continuously ingests live telemetry from AWS CDS.",
                "voice": "Our autonomous agent continuously ingests live telemetry from AWS Communication Developer Services."
            },
            {
                "text": "Sub-5 millisecond response establishes a clean deterministic baseline.",
                "voice": "Sub-5 millisecond response establishes a clean deterministic baseline."
            }
        ],
        "log_stream": [
            "[INGRESS] Connected to AWS CDS Event Bridge: Endpoint api.telecom.aws-cds.internal",
            "[TELEMETRY] Scanning 10,000 TPS real-time stream across global carrier trunks...",
            "[SRE GUARD] Continuous health probes active across US-East, EU-West, and AP-Northeast.",
            "[STATUS] Nominal baseline verified. Packet drop rate = 0.00%, Latency = 6.42ms."
        ],
        "active_card_idx": 0,
        "base_metrics": {"lat": 6.42, "drop": "0.00%", "route": "CARRIER_ALPHA"}
    },
    {
        "act_id": "ACT 2: CHAOS FAULT INJECTION & ANOMALY SURGE",
        "sentences": [
            {
                "text": "Extreme chaos fault injected into Carrier Alpha primary trunk.",
                "voice": "Extreme chaos fault injected into Carrier Alpha primary trunk."
            },
            {
                "text": "Transient packet drop spike of 8.5% exceeds critical safety threshold.",
                "voice": "Transient packet drop spike of eight point five percent exceeds critical safety threshold."
            },
            {
                "text": "Anomaly detector isolates the degrading communication trunk instantly.",
                "voice": "Anomaly detector isolates the degrading communication trunk instantly."
            },
            {
                "text": "Nominal routing is frozen in 4.8 milliseconds to protect subscriber SLA.",
                "voice": "Nominal routing is frozen in four point eight milliseconds to protect subscriber SLA."
            }
        ],
        "log_stream": [
            "[CHAOS INJECTION] Injected packet drop spike: 8.5% on Carrier Alpha Primary Trunk",
            "[ANOMALY DETECTED] Threshold exceeded: Packet drop 8.5% > 2.0% ASIL-D margin!",
            "[DAMPING FILTER] Isolating transient burst: Confirmed persistent carrier outage.",
            "[ESCALATION] Packaging real-time network topology graph to Amazon Bedrock AgentCore."
        ],
        "active_card_idx": 1,
        "base_metrics": {"lat": 48.50, "drop": "8.50%", "route": "FAILING_TRUNK"}
    },
    {
        "act_id": "ACT 3: AMAZON BEDROCK AUTONOMOUS REASONING",
        "sentences": [
            {
                "text": "Amazon Bedrock AgentCore invokes Claude 3.5 Sonnet for topology analysis.",
                "voice": "Amazon Bedrock AgentCore invokes Claude three point five Sonnet for topology analysis."
            },
            {
                "text": "Evaluating secondary route bandwidth and multi-carrier peering QoS matrices.",
                "voice": "Evaluating secondary route bandwidth and multi-carrier peering Q, o, S matrices."
            },
            {
                "text": "Bedrock synthesizes root-cause mitigation plan in 3.12 milliseconds.",
                "voice": "Bedrock synthesizes root-cause mitigation plan in three point one two milliseconds."
            },
            {
                "text": "Authorizing instant dynamic failover to AWS End User Messaging secondary trunk.",
                "voice": "Authorizing instant dynamic failover to AWS End User Messaging secondary trunk."
            }
        ],
        "log_stream": [
            "[BEDROCK REASONING] AgentCore invoked Claude 3.5 Sonnet: Model ID anthropic.claude-v2",
            "[TOPOLOGY ANALYSIS] Evaluating secondary route bandwidth and peering QoS matrices...",
            "[SYNTHESIS] Root cause identified as upstream fiber cut. Route bypass computed in 3.12ms.",
            "[DECISION COMMITTED] Authorizing instant failover to AWS CDS secondary carrier route."
        ],
        "active_card_idx": 2,
        "base_metrics": {"lat": 32.10, "drop": "4.20%", "route": "BEDROCK_DECISION"}
    },
    {
        "act_id": "ACT 4: DYNAMIC CARRIER FAILOVER & AWS EUM DISPATCH",
        "sentences": [
            {
                "text": "Executing deterministic zero-packet-drop circuit migration.",
                "voice": "Executing deterministic zero-packet-drop circuit migration."
            },
            {
                "text": "Traffic rerouted smoothly to AWS CDS secondary communication trunk.",
                "voice": "Traffic rerouted smoothly to AWS CDS secondary communication trunk."
            },
            {
                "text": "AWS End User Messaging dispatches multi-channel SMS and RCS alerts.",
                "voice": "AWS End User Messaging dispatches multi-channel SMS and RCS alerts."
            },
            {
                "text": "Telemetry stabilized on secondary path. Latency normalized to 7.15ms.",
                "voice": "Telemetry stabilized on secondary path. Latency normalized to seven point one five milliseconds."
            }
        ],
        "log_stream": [
            "[CIRCUIT SWITCH] Migrating backbone traffic from Carrier Alpha to AWS CDS Secondary Trunk.",
            "[EUM DISPATCH] AWS End User Messaging SMS alert sent to NOC: MSG-AWS-CDS-179269.",
            "[RCS BROADCAST] Verified carrier acknowledgment: DELIVERED_CARRIER_ACK.",
            "[RESTORED] Telemetry stabilized on secondary trunk. Latency normalized to 7.15ms."
        ],
        "active_card_idx": 2,
        "base_metrics": {"lat": 7.15, "drop": "0.00%", "route": "AWS_CDS_ROUTE"}
    },
    {
        "act_id": "ACT 5: ASIL-D 50GB CIRCUIT BREAKER & ZDR CLOSURE",
        "sentences": [
            {
                "text": "Phase four governance: Auditing memory against 50GB ASIL-D limit.",
                "voice": "Phase four governance: Auditing memory against fifty gigabyte ASIL-D limit."
            },
            {
                "text": "Executing 2-Pass cryptographic zero-data-residue memory scrub.",
                "voice": "Executing two-pass cryptographic zero-data-residue memory scrub."
            },
            {
                "text": "Bitwise memory purged cleanly with zero byte residual footprint.",
                "voice": "Bitwise memory purged cleanly with zero byte residual footprint."
            },
            {
                "text": "Official Verdict: All 4 Tasks Passed. System is 100% Production Ready.",
                "voice": "Official Verdict: All 4 Tasks Passed. System is one hundred percent Production Ready."
            }
        ],
        "log_stream": [
            "[ASIL-D MONITOR] Memory ceiling verified: 2.15GB nominal / 50.0GB safety limit.",
            "[GOVERNANCE PURGE] Executing 2-Pass ZDR Memory Scrub (0xAA -> 0x00)...",
            "[ZDR VERIFIED] Residual Memory = 0.000000 MB | WORM Receipt = PG-RECEIPT-TELCO-TASK-0x99A1",
            "OFFICIAL VERDICT: [ ALL 4 TASKS PASSED - PRODUCTION READY ]"
        ],
        "active_card_idx": 3,
        "base_metrics": {"lat": 0.04, "drop": "0.00%", "route": "ZDR_PURGED"}
    }
]

def get_font(size: int):
    try:
        return ImageFont.truetype("arialbd.ttf", size)
    except Exception:
        return ImageFont.load_default()

def get_font_mono(size: int):
    try:
        return ImageFont.truetype("consola.ttf", size)
    except Exception:
        return ImageFont.load_default()

def synthesize_single_sentence(text: str, output_wav: Path):
    clean_text = text.replace("'", "").replace('"', '').replace("\n", " ")
    ps_cmd = (
        f"Add-Type -AssemblyName System.Speech; "
        f"$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
        f"$installed = $synth.GetInstalledVoices(); "
        f"$zira = $installed | Where-Object {{ $_.VoiceInfo.Name -like '*Zira*' }}; "
        f"if ($zira) {{ $synth.SelectVoice($zira.VoiceInfo.Name) }} "
        f"else {{ $synth.SelectVoiceByHints([System.Speech.Synthesis.VoiceGender]::Female) }}; "
        f"$synth.Rate = -1; "
        f"$synth.Volume = 100; "
        f"$synth.SetOutputToWaveFile('{str(output_wav).replace(os.sep, '/')}'); "
        f"$synth.Speak('{clean_text}'); "
        f"$synth.Dispose();"
    )
    subprocess.run(["powershell", "-NoProfile", "-Command", ps_cmd], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def get_wav_duration(wav_path: Path) -> float:
    cmd = [
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1",
        str(wav_path)
    ]
    res = subprocess.run(cmd, capture_output=True, text=True)
    try:
        return float(res.stdout.strip())
    except Exception:
        return 4.0

def render_hollywood_frame(act_data: dict, act_num: int, current_cursor: float, f_idx: int, frame_path: Path):
    sentences = [s["text"] for s in act_data["sentences"]]
    num_sentences = len(sentences)

    jitter = math.sin(f_idx * 0.45) * 0.08
    live_lat = max(0.01, act_data["base_metrics"]["lat"] + jitter)

    img = Image.new("RGB", (WIDTH, HEIGHT), (8, 12, 22))
    draw = ImageDraw.Draw(img)

    # 1. TOP HEADER SAFE AREA
    header_y1, header_y2 = 40, 160
    draw.rectangle([60, header_y1, WIDTH - 60, header_y2], fill=(15, 23, 42), outline=(0, 229, 255), width=3)
    draw.text((90, 62), "PHANToM GRID 2.0 // AWS CDS AUTONOMOUS TELCO SRE", font=get_font(40), fill=(255, 255, 255))
    draw.text((90, 114), act_data["act_id"], font=get_font(24), fill=(0, 229, 255))

    pulse_col = (16, 185, 129) if (f_idx % 20 < 10) else (5, 150, 105)
    draw.ellipse([1850, 84, 1880, 114], fill=pulse_col)
    draw.text((1895, 78), "ASIL-D FUNCTIONAL SAFETY", font=get_font(36), fill=(16, 185, 129))

    # 2. LEFT CONTAINER: DYNAMIC TUI TERMINAL
    tui_x1, tui_y1 = 60, 180
    tui_x2, tui_y2 = 1680, 1030
    draw.rectangle([tui_x1, tui_y1, tui_x2, tui_y2], fill=(6, 9, 16), outline=(56, 189, 248), width=2)
    draw.rectangle([tui_x1, tui_y1, tui_x2, tui_y1 + 65], fill=(15, 23, 42))
    draw.text((90, tui_y1 + 18), f"TERMINAL TELEMETRY & EVENT STREAM :: [ACT {act_num}/5]", font=get_font(26), fill=(0, 229, 255))

    active_log_idx = min(int(current_cursor), len(act_data["log_stream"]) - 1)
    for l_idx, log in enumerate(act_data["log_stream"]):
        y_log = tui_y1 + 105 + (l_idx * 90)
        is_active = (l_idx == active_log_idx)

        if is_active:
            draw.rectangle([tui_x1 + 20, y_log - 10, tui_x2 - 20, y_log + 52], fill=(24, 38, 64), outline=(0, 229, 255), width=2)
            draw.text((tui_x1 + 35, y_log), ">", font=get_font_mono(32), fill=(251, 191, 36))
            log_col = (255, 255, 255)
        else:
            log_col = (148, 163, 184) if l_idx > active_log_idx else (226, 232, 240)

        if "PASS" in log or "Nominal" in log or "RESTORED" in log:
            log_col = (16, 185, 129)
        elif "CHAOS" in log or "ANOMALY" in log:
            log_col = (239, 68, 68)

        draw.text((tui_x1 + 75, y_log), log, font=get_font_mono(27), fill=log_col)

    # 3. RIGHT CONTAINER: GAUGES & METRICS
    radar_x1, radar_x2 = 1710, WIDTH - 60
    draw.rectangle([radar_x1, tui_y1, radar_x2, tui_y2], fill=(15, 23, 42), outline=(168, 85, 247), width=2)
    draw.rectangle([radar_x1, tui_y1, radar_x2, tui_y1 + 65], fill=(30, 27, 75))
    draw.text((radar_x1 + 30, tui_y1 + 18), "REAL-TIME ACTIVE STATUS GAUGES", font=get_font(26), fill=(168, 85, 247))

    cards = [
        ("TELEMETRY LATENCY", f"{live_lat:.2f} ms", (0, 229, 255)),
        ("FAULT MONITOR", act_data["base_metrics"]["drop"], (239, 68, 68) if "8.5" in act_data["base_metrics"]["drop"] else (16, 185, 129)),
        ("ACTIVE ROUTING", act_data["base_metrics"]["route"], (168, 85, 247)),
        ("MEMORY RESIDUE", "0.000000 MB", (16, 185, 129))
    ]

    active_card = act_data["active_card_idx"]
    card_h = 175
    for c_idx, (title, val, c_col) in enumerate(cards):
        cy = tui_y1 + 80 + (c_idx * (card_h + 16))
        is_card_active = (c_idx == active_card)
        card_outline = (251, 191, 36) if is_card_active else c_col
        card_fill = (26, 38, 68) if is_card_active else (8, 12, 22)

        draw.rectangle([radar_x1 + 25, cy, radar_x2 - 25, cy + card_h], fill=card_fill, outline=card_outline, width=3 if is_card_active else 1)
        
        if is_card_active:
            draw.rectangle([radar_x1 + 45, cy + 18, radar_x1 + 170, cy + 48], fill=(251, 191, 36))
            draw.text((radar_x1 + 52, cy + 22), "LIVE FOCUS", font=get_font(18), fill=(10, 15, 27))
            draw.text((radar_x1 + 185, cy + 22), title, font=get_font(22), fill=(255, 255, 255))
        else:
            draw.text((radar_x1 + 45, cy + 22), title, font=get_font(22), fill=(148, 163, 184))

        draw.text((radar_x1 + 45, cy + 72), val, font=get_font(56), fill=card_outline)

    # 4. BOTTOM CONTAINER: CLEAN TELEPROMPTER STREAM (NO SUB-BOX)
    box_y1 = 1055
    box_y2 = 1405
    box_x1 = 60
    box_x2 = WIDTH - 60

    draw.rectangle([box_x1, box_y1, box_x2, box_y2], fill=(11, 16, 29))
    
    # Inset header strip
    title_strip_h = 65
    draw.rectangle([box_x1 + 6, box_y1 + 6, box_x2 - 6, box_y1 + title_strip_h], fill=(22, 33, 56))
    draw.text((box_x1 + 35, box_y1 + 14), "[AI NARRATOR LIVE TELEPROMPTER // BROADCAST STREAM]", font=get_font(36), fill=(245, 158, 11))

    slot_height = 125
    base_center_y = box_y1 + 185

    for s_idx, sentence_text in enumerate(sentences):
        y_offset = (s_idx - current_cursor) * slot_height
        render_y = base_center_y + y_offset

        if render_y < box_y1 + 75 or render_y > box_y2 - 65:
            continue

        dist_from_focus = abs(s_idx - current_cursor)

        if dist_from_focus < 0.5:
            # FOCUS SENTENCE: Pure 56pt Bold White + Golden Pointer (NO SUB-BOX)
            draw.text((box_x1 + 45, render_y), ">", font=get_font(56), fill=(251, 191, 36))
            draw.text((box_x1 + 105, render_y), sentence_text, font=get_font(56), fill=(255, 255, 255))
        else:
            # UPCOMING/HISTORY: 30pt Medium Gray-Blue
            fade_alpha = max(0.2, 1.0 - (dist_from_focus * 0.45))
            gray_val = int(148 * fade_alpha)
            draw.text((box_x1 + 105, render_y + 12), sentence_text, font=get_font(30), fill=(gray_val, gray_val + 10, gray_val + 20))

    # FINAL SEAL: GUARANTEE BORDER INTEGRITY (PHYSICAL SEAL)
    draw.rectangle([box_x1, box_y1, box_x2, box_y2], outline=(251, 191, 36), width=4)
    draw.line([(box_x1, box_y1), (box_x2, box_y1)], fill=(251, 191, 36), width=5)

    img.save(frame_path, "PNG")

def compile_full_demo_video():
    print("=" * 80)
    print("PHANToM GRID // COMPILING BROADCAST VIDEO (CLEAN STREAM / NO SUB-BOX)")
    print("=" * 80)
    TEMP_DIR.mkdir(parents=True, exist_ok=True)
    act_video_parts = []
    fps = 10

    for a_idx, act in enumerate(ACTS):
        act_num = a_idx + 1
        print(f"\n--- [PROCESSING ACT {act_num}/5: {act['act_id']}] ---")
        act_frame_dir = TEMP_DIR / f"act_{act_num}_frames"
        act_frame_dir.mkdir(parents=True, exist_ok=True)

        sentence_durations = []
        sentence_wavs = []
        for s_idx, sent_obj in enumerate(act["sentences"]):
            sent_wav = TEMP_DIR / f"act_{act_num}_sent_{s_idx}.wav"
            print(f"  [*] Synthesizing Sentence {s_idx + 1}/4...")
            synthesize_single_sentence(sent_obj["voice"], sent_wav)
            dur = get_wav_duration(sent_wav)
            sentence_durations.append(dur)
            sentence_wavs.append(sent_wav)
            print(f"      Duration: {dur:.2f}s -> '{sent_obj['text'][:40]}...'")

        act_concat_list = TEMP_DIR / f"act_{act_num}_audio_concat.txt"
        with open(act_concat_list, "w", encoding="utf-8") as f:
            for sw in sentence_wavs:
                f.write(f"file '{sw.resolve().as_posix()}'\n")

        raw_act_audio = TEMP_DIR / f"act_{act_num}_raw_audio.wav"
        subprocess.run([
            "ffmpeg", "-y", "-f", "concat", "-safe", "0",
            "-i", str(act_concat_list),
            "-c", "copy", str(raw_act_audio)
        ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        total_act_duration = sum(sentence_durations)
        print(f"  [+] Act {act_num} Total Exact Duration: {total_act_duration:.2f}s")

        mixed_act_audio = TEMP_DIR / f"act_{act_num}_mixed_audio.wav"
        synth_ambience_cmd = [
            "ffmpeg", "-y",
            "-i", str(raw_act_audio),
            "-f", "lavfi", "-i", f"sine=frequency=110:duration={total_act_duration + 0.5}",
            "-filter_complex",
            "[1:a]volume=0.03,lowpass=f=200[bed];[0:a]afade=t=in:ss=0:d=0.06,afade=t=out:st=" + f"{max(0, total_act_duration - 0.08)}:d=0.08[vox];[vox][bed]amix=inputs=2:duration=first[out]",
            "-map", "[out]",
            "-c:a", "pcm_s16le",
            str(mixed_act_audio)
        ]
        res_mix = subprocess.run(synth_ambience_cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        effective_audio = mixed_act_audio if (res_mix.returncode == 0 and mixed_act_audio.exists()) else raw_act_audio

        time_checkpoints = [0.0]
        accum_t = 0.0
        for dur in sentence_durations:
            accum_t += dur
            time_checkpoints.append(accum_t)

        total_frames = int(total_act_duration * fps)
        print(f"  [*] Rendering {total_frames} Frames with Clean Stream...")

        for f_idx in range(total_frames):
            curr_sec = f_idx / fps

            active_s = 0
            for i in range(len(sentence_durations)):
                if curr_sec >= time_checkpoints[i] and curr_sec < time_checkpoints[i + 1]:
                    active_s = i
                    break
            else:
                active_s = len(sentence_durations) - 1

            sent_start = time_checkpoints[active_s]
            sent_end = time_checkpoints[active_s + 1]
            time_remaining = sent_end - curr_sec

            if time_remaining < 0.35 and active_s < len(sentence_durations) - 1:
                scroll_prog = (0.35 - time_remaining) / 0.35
                cursor = active_s + scroll_prog
            else:
                cursor = float(active_s)

            frame_png = act_frame_dir / f"f_{f_idx:04d}.png"
            render_hollywood_frame(act, act_num, cursor, f_idx, frame_png)

        act_mp4 = TEMP_DIR / f"act_{act_num}_segment.mp4"
        print(f"  [*] Encoding Act {act_num} Segment...")
        cmd_segment = [
            "ffmpeg", "-y",
            "-framerate", str(fps),
            "-i", str(act_frame_dir / "f_%04d.png"),
            "-i", str(effective_audio),
            "-c:v", "libx264",
            "-c:a", "aac", "-b:a", "192k",
            "-pix_fmt", "yuv420p",
            "-shortest",
            str(act_mp4)
        ]
        subprocess.run(cmd_segment, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        act_video_parts.append(act_mp4)
        print(f"  [+] Act {act_num} Segment Ready: {act_mp4.name}")

    concat_list_file = TEMP_DIR / "master_concat_list.txt"
    with open(concat_list_file, "w", encoding="utf-8") as f:
        for vp in act_video_parts:
            f.write(f"file '{vp.resolve().as_posix()}'\n")

    print("\n[*] Concatenating 5 Acts into Final Broadcast Master MP4...")
    cmd_concat = [
        "ffmpeg", "-y",
        "-f", "concat", "-safe", "0",
        "-i", str(concat_list_file),
        "-c", "copy",
        str(OUTPUT_MP4)
    ]
    subprocess.run(cmd_concat, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    import shutil
    shutil.rmtree(TEMP_DIR, ignore_errors=True)

    size_mb = OUTPUT_MP4.stat().st_size / (1024 * 1024)
    print("=" * 80)
    print(f"[+] CLEAN STREAM MASTER GENERATED: {OUTPUT_MP4}")
    print(f"[+] FILE SIZE: {size_mb:.2f} MB")
    print("[+] UPGRADE: Cyan Sub-Box Removed, Golden Pointer Focus, Pure Typography")
    print("=" * 80)

if __name__ == "__main__":
    compile_full_demo_video()
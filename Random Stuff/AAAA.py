'''
# Project Creation Date: 10:05:46 PM, 3/01/2026
'''

#!/usr/bin/env python3
"""
Temporal Frame Difference Video Processor
Creates a motion-capture effect by blending inverted frames with time-offset duplicates.
"""

import cv2
import numpy as np
import argparse
from pathlib import Path


def process_video(input_path, output_path, time_offset=0.05, opacity=0.5, invert=True):
    """
    Apply temporal frame differencing effect to video.
    
    Args:
        input_path: Path to input video
        output_path: Path to save output video
        time_offset: Time offset in seconds between frames (default 0.05)
        opacity: Opacity/blend factor for frames (0-1, default 0.5)
        invert: Whether to invert colors (default True)
    """
    
    # Open input video
    cap = cv2.VideoCapture(str(input_path))
    if not cap.isOpened():
        raise ValueError(f"Could not open video: {input_path}")
    
    # Get video properties
    fps = cap.get(cv2.CAP_PROP_FPS)
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    
    # Calculate frame offset
    frame_offset = max(1, int(fps * time_offset))
    
    print(f"Processing video:")
    print(f"  Resolution: {width}x{height}")
    print(f"  FPS: {fps}")
    print(f"  Total frames: {total_frames}")
    print(f"  Frame offset: {frame_offset} frames ({time_offset}s)")
    
    # Setup output video writer
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(str(output_path), fourcc, fps, (width, height))
    
    # Buffer to store frames for temporal offset
    frame_buffer = []
    
    frame_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Add current frame to buffer
        frame_buffer.append(frame.copy())
        
        # Once we have enough frames for the offset
        if len(frame_buffer) > frame_offset:
            # Get current and offset frame
            current_frame = frame_buffer[-1]
            offset_frame = frame_buffer[-frame_offset - 1]
            
            # Invert colors if requested
            if invert:
                current_frame = cv2.bitwise_not(current_frame)
                offset_frame = cv2.bitwise_not(offset_frame)
            
            # Blend frames with opacity
            blended = cv2.addWeighted(current_frame, opacity, offset_frame, opacity, 0)
            
            # Write output frame
            out.write(blended)
            
            frame_count += 1
            if frame_count % 30 == 0:
                progress = (frame_count / (total_frames - frame_offset)) * 100
                print(f"  Progress: {progress:.1f}%", end='\r')
        
        # Keep buffer manageable
        if len(frame_buffer) > frame_offset + 10:
            frame_buffer.pop(0)
    
    print(f"\n  Processed {frame_count} frames")
    
    # Cleanup
    cap.release()
    out.release()
    print(f"\nOutput saved to: {output_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Apply temporal frame differencing for motion capture effect",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s input.mp4 output.mp4
  %(prog)s input.mp4 output.mp4 --offset 0.1 --opacity 0.6 --no-invert
        """
    )
    
    parser.add_argument('input', type=str, help='Input video file')
    parser.add_argument('output', type=str, help='Output video file')
    parser.add_argument('--offset', type=float, default=0.05,
                        help='Time offset in seconds (default: 0.05)')
    parser.add_argument('--opacity', type=float, default=0.5,
                        help='Blend opacity 0-1 (default: 0.5)')
    parser.add_argument('--no-invert', action='store_true',
                        help='Disable color inversion')
    
    args = parser.parse_args()
    
    # Validate inputs
    input_path = Path(args.input)
    if not input_path.exists():
        print(f"Error: Input file not found: {input_path}")
        return 1
    
    output_path = Path(args.output)
    
    # Validate parameters
    if not 0 < args.opacity <= 1:
        print("Error: Opacity must be between 0 and 1")
        return 1
    
    if args.offset <= 0:
        print("Error: Time offset must be positive")
        return 1
    
    try:
        process_video(
            input_path,
            output_path,
            time_offset=args.offset,
            opacity=args.opacity,
            invert=not args.no_invert
        )
        return 0
    except Exception as e:
        print(f"\nError processing video: {e}")
        return 1


if __name__ == '__main__':
    exit(main())
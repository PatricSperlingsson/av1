import subprocess

# Path to the uploaded AVIF file
avif_file_path = "original_image_smooth.avif"

# Run ffprobe to analyze the AVIF file bitstream
ffprobe_cmd = [
    "ffprobe",
    "-show_streams",
    "-show_format",
    "-print_format", "json",
    avif_file_path
]

try:
    result = subprocess.run(ffprobe_cmd, capture_output=True, text=True, check=True)
    ffprobe_output = result.stdout
except subprocess.CalledProcessError as e:
    ffprobe_output = f"Error running ffprobe: {e}"

ffprobe_output[:1000]  # Show first 1000 characters of the output for analysis.
print(f"ffprobe_output: {ffprobe_output}")

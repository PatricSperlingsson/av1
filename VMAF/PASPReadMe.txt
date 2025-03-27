cd D:\Patric\MinaDokument\GitHub\av1
D:/Patric/ffmpeg/bin/ffmpeg.exe -i "D:/Patric/ffmpeg/quantized_video.mp4" -i "D:/Patric/ffmpeg/original_video.mp4" -lavfi "libvmaf=model='path=D\\\:/Patric/MinaDokument/GitHub/vmaf/model/vmaf_float_v0.6.1.json':log_path='D\\\:/Patric/ffmpeg/vmaf_log.json':log_fmt=json" -f null - -loglevel debug

ffmpeg version N-118380-gca3550948c-20250129 Copyright (c) 2000-2025 the FFmpeg developers
  built with gcc 14.2.0 (crosstool-NG 1.26.0.120_4d36f27)
  configuration: --prefix=/ffbuild/prefix --pkg-config-flags=--static --pkg-config=pkg-config --cross-prefix=x86_64-w64-mingw32- --arch=x86_64 --target-os=mingw32 --enable-gpl --enable-version3 --disable-debug --enable-shared --disable-static --disable-w32threads --enable-pthreads --enable-iconv --enable-zlib --enable-libfreetype --enable-libfribidi --enable-gmp --enable-libxml2 --enable-lzma --enable-fontconfig --enable-libharfbuzz --enable-libvorbis --enable-opencl --disable-libpulse --enable-libvmaf --disable-libxcb --disable-xlib --enable-amf --enable-libaom --enable-libaribb24 --enable-avisynth --enable-chromaprint --enable-libdav1d --enable-libdavs2 --enable-libdvdread --enable-libdvdnav --disable-libfdk-aac --enable-ffnvcodec --enable-cuda-llvm --enable-frei0r --enable-libgme --enable-libkvazaar --enable-libaribcaption --enable-libass --enable-libbluray --enable-libjxl --enable-libmp3lame --enable-libopus --enable-librist --enable-libssh --enable-libtheora --enable-libvpx --enable-libwebp --enable-libzmq --enable-lv2 --enable-libvpl --enable-openal --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-libopenh264 --enable-libopenjpeg --enable-libopenmpt --enable-librav1e --enable-librubberband --enable-schannel --enable-sdl2 --enable-libsnappy --enable-libsoxr --enable-libsrt --enable-libsvtav1 --enable-libtwolame --enable-libuavs3d --disable-libdrm --enable-vaapi --enable-libvidstab --enable-vulkan --enable-libshaderc --enable-libplacebo --disable-libvvenc --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxvid --enable-libzimg --enable-libzvbi --extra-cflags=-DLIBTWOLAME_STATIC --extra-cxxflags= --extra-libs=-lgomp --extra-ldflags=-pthread --extra-ldexeflags= --cc=x86_64-w64-mingw32-gcc --cxx=x86_64-w64-mingw32-g++ --ar=x86_64-w64-mingw32-gcc-ar --ranlib=x86_64-w64-mingw32-gcc-ranlib --nm=x86_64-w64-mingw32-gcc-nm --extra-version=20250129
  libavutil      59. 56.100 / 59. 56.100
  libavcodec     61. 31.101 / 61. 31.101
  libavformat    61.  9.106 / 61.  9.106
  libavdevice    61.  4.100 / 61.  4.100
  libavfilter    10.  9.100 / 10.  9.100
  libswscale      8. 13.100 /  8. 13.100
  libswresample   5.  4.100 /  5.  4.100
  libpostproc    58.  4.100 / 58.  4.100
Splitting the commandline.
Reading option '-i' ... matched as input url with argument 'D:/Patric/ffmpeg/quantized_video.mp4'.
Reading option '-i' ... matched as input url with argument 'D:/Patric/ffmpeg/original_video.mp4'.
Reading option '-lavfi' ... matched as option 'lavfi' (create a complex filtergraph) with argument 'libvmaf=model='path=D\\\:/Patric/MinaDokument/GitHub/vmaf/model/vmaf_float_v0.6.1.json':log_path='D\\\:/Patric/ffmpeg/vmaf_log.json':log_fmt=json'.
Reading option '-f' ... matched as option 'f' (force container format (auto-detected otherwise)) with argument 'null'.
Reading option '-' ... matched as output url.
Reading option '-loglevel' ... matched as option 'loglevel' (set logging level) with argument 'debug'.
Finished splitting the commandline.
Parsing a group of options: global .
Applying option lavfi (create a complex filtergraph) with argument libvmaf=model='path=D\\\:/Patric/MinaDokument/GitHub/vmaf/model/vmaf_float_v0.6.1.json':log_path='D\\\:/Patric/ffmpeg/vmaf_log.json':log_fmt=json.
Applying option loglevel (set logging level) with argument debug.
Successfully parsed a group of options.
[AVFilterGraph @ 000001c3ced4c4c0] Setting 'model' to value 'path=D\:/Patric/MinaDokument/GitHub/vmaf/model/vmaf_float_v0.6.1.json'
[AVFilterGraph @ 000001c3ced4c4c0] Setting 'log_path' to value 'D\:/Patric/ffmpeg/vmaf_log.json'
[AVFilterGraph @ 000001c3ced4c4c0] Setting 'log_fmt' to value 'json'
libvmaf DEBUG feature extractor "float_adm" registered with 0 opts
libvmaf DEBUG feature extractor "float_motion" registered with 0 opts
libvmaf DEBUG feature extractor "float_vif" registered with 0 opts
Parsing a group of options: input url D:/Patric/ffmpeg/quantized_video.mp4.
Successfully parsed a group of options.
Opening an input file: D:/Patric/ffmpeg/quantized_video.mp4.
[AVFormatContext @ 000001c3ced51e00] Opening 'D:/Patric/ffmpeg/quantized_video.mp4' for reading
[file @ 000001c3ced50480] Setting default whitelist 'file,crypto,data'
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Format mov,mp4,m4a,3gp,3g2,mj2 probed with size=2048 and score=100
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] ISO: File Type Major Brand: isom
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Unknown dref type 0x206c7275 size 12
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Processing st: 0, edit list 0 - media time: 1024, duration: 12800
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Offset DTS by 1024 to make first pts zero.
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Setting codecpar->delay to 2 for stream st: 0
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] Before avformat_find_stream_info() pos: 16730 bytes read:16730 seeks:0 nb_streams:1
[h264 @ 000001c3cee10380] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3cee10380] Decoding VUI
[h264 @ 000001c3cee10380] nal_unit_type: 8(PPS), nal_ref_idc: 3
[h264 @ 000001c3cee10380] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3cee10380] Decoding VUI
[h264 @ 000001c3cee10380] nal_unit_type: 8(PPS), nal_ref_idc: 3
[h264 @ 000001c3cee10380] nal_unit_type: 6(SEI), nal_ref_idc: 0
[h264 @ 000001c3cee10380] nal_unit_type: 5(IDR), nal_ref_idc: 3
[h264 @ 000001c3cee10380] Format yuv420p chosen by get_format().
[h264 @ 000001c3cee10380] Reinit context to 416x432, pix_fmt: yuv420p
[h264 @ 000001c3cee10380] no picture
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] All info found
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced51e00] After avformat_find_stream_info() pos: 15042 bytes read:16730 seeks:0 frames:1
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'D:/Patric/ffmpeg/quantized_video.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf61.9.106
  Duration: 00:00:01.00, start: 0.000000, bitrate: 133 kb/s
  Stream #0:0[0x1](und), 1, 1/12800: Video: h264 (High), 1 reference frame (avc1 / 0x31637661), yuv420p(progressive, left), 414x420, 0/1, 124 kb/s, 25 fps, 25 tbr, 12800 tbn (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
      encoder         : Lavc61.31.101 libx264
Successfully opened the file.
Parsing a group of options: input url D:/Patric/ffmpeg/original_video.mp4.
Successfully parsed a group of options.
Opening an input file: D:/Patric/ffmpeg/original_video.mp4.
[AVFormatContext @ 000001c3d0fead00] Opening 'D:/Patric/ffmpeg/original_video.mp4' for reading
[file @ 000001c3ced4c4c0] Setting default whitelist 'file,crypto,data'
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Format mov,mp4,m4a,3gp,3g2,mj2 probed with size=2048 and score=100
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] ISO: File Type Major Brand: isom
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Unknown dref type 0x206c7275 size 12
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Processing st: 0, edit list 0 - media time: 1024, duration: 12800
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Offset DTS by 1024 to make first pts zero.
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Setting codecpar->delay to 2 for stream st: 0
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] Before avformat_find_stream_info() pos: 19293 bytes read:19293 seeks:0 nb_streams:1
[h264 @ 000001c3cee257c0] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3cee257c0] Decoding VUI
[h264 @ 000001c3cee257c0] nal_unit_type: 8(PPS), nal_ref_idc: 3
[h264 @ 000001c3cee257c0] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3cee257c0] Decoding VUI
[h264 @ 000001c3cee257c0] nal_unit_type: 8(PPS), nal_ref_idc: 3
[h264 @ 000001c3cee257c0] nal_unit_type: 6(SEI), nal_ref_idc: 0
[h264 @ 000001c3cee257c0] nal_unit_type: 5(IDR), nal_ref_idc: 3
[h264 @ 000001c3cee257c0] Format yuv420p chosen by get_format().
[h264 @ 000001c3cee257c0] Reinit context to 416x432, pix_fmt: yuv420p
[h264 @ 000001c3cee257c0] no picture
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] All info found
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3d0fead00] After avformat_find_stream_info() pos: 17687 bytes read:19293 seeks:0 frames:1
Input #1, mov,mp4,m4a,3gp,3g2,mj2, from 'D:/Patric/ffmpeg/original_video.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf61.9.106
  Duration: 00:00:01.00, start: 0.000000, bitrate: 154 kb/s
  Stream #1:0[0x1](und), 1, 1/12800: Video: h264 (High), 1 reference frame (avc1 / 0x31637661), yuv420p(progressive, left), 414x420, 0/1, 145 kb/s, 25 fps, 25 tbr, 12800 tbn (default)
    Metadata:
      handler_name    : VideoHandler
      vendor_id       : [0][0][0][0]
      encoder         : Lavc61.31.101 libx264
Successfully opened the file.
Parsing a group of options: output url -.
Applying option f (force container format (auto-detected otherwise)) with argument null.
Successfully parsed a group of options.
Opening an output file: -.
[out#0/null @ 000001c3cedba740] Creating output stream from unlabeled output of complex filtergraph 0. This overrides automatic video mapping.
[vost#0:0/wrapped_avframe @ 000001c3cee22c40] Created video stream from complex filtergraph 0:[libvmaf:default]
[vost#0:0/wrapped_avframe @ 000001c3cee22c40]
[out#0/null @ 000001c3cedba740] No explicit maps, mapping streams automatically...
Successfully opened the file.
[fc#0 @ 000001c3cedd9bc0] Binding unlabeled input 0 to input stream 0:0
detected 28 logical cores
[h264 @ 000001c3d0f311c0] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3d0f311c0] Decoding VUI
[h264 @ 000001c3d0f311c0] nal_unit_type: 8(PPS), nal_ref_idc: 3
[fc#0 @ 000001c3cedd9bc0] Binding unlabeled input 1 to input stream 1:0
[h264 @ 000001c3d1031940] nal_unit_type: 7(SPS), nal_ref_idc: 3
[h264 @ 000001c3d1031940] Decoding VUI
[h264 @ 000001c3d1031940] nal_unit_type: 8(PPS), nal_ref_idc: 3
Stream mapping:
  Stream #0:0 (h264) -> libvmaf
  Stream #1:0 (h264) -> libvmaf
  libvmaf:default -> Stream #0:0 (wrapped_avframe)
[vost#0:0/wrapped_avframe @ 000001c3cee22c40] Starting thread...
[fc#0 @ 000001c3cedd9bc0] Starting thread...
[vist#0:0/h264 @ 000001c3cee12200] [dec:h264 @ 000001c3cee25980] Starting thread...
[vist#1:0/h264 @ 000001c3cee257c0] [dec:h264 @ 000001c3d1cf9a80] Starting thread...
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80] Starting thread...
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080] Starting thread...
Press [q] to stop, [?] for help
[h264 @ 000001c3d0f311c0] nal_unit_type: 6(SEI), nal_ref_idc: 0
[h264 @ 000001c3d0f311c0] nal_unit_type: 5(IDR), nal_ref_idc: 3
[h264 @ 000001c3d0f311c0] Format yuv420p chosen by get_format().
[h264 @ 000001c3d0f311c0] Reinit context to 416x432, pix_fmt: yuv420p
[h264 @ 000001c3d0f311c0] no picture
[h264 @ 000001c3d11b2680] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d11b2680] no picture
[h264 @ 000001c3d0e3e680] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3cee1a200] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d13dd840] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d14f8a40] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d15b1fc0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d166af00] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1723e80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d0eefdc0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d0f0cd00] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d194f900] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1a08840] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1030e40] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d1031d00] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80] EOF while reading input
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80] Terminating thread with return code 0 (success)
[h264 @ 000001c3d1032440] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d0f311c0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d11b2680] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d1031940] nal_unit_type: 6(SEI), nal_ref_idc: 0
[h264 @ 000001c3d0e3e680] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d1031940] nal_unit_type: 5(IDR), nal_ref_idc: 3
[h264 @ 000001c3d1031940] Format yuv420p chosen by get_format().
[h264 @ 000001c3d1031940] Reinit context to 416x432, pix_fmt: yuv420p
[h264 @ 000001c3cee1a200] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1031940] no picture
[h264 @ 000001c3d13dd840] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1032080] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d14f8a40] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d1032080] no picture
[h264 @ 000001c3d15b1fc0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d1030a80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d166af00] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d10311c0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[vist#0:0/h264 @ 000001c3cee12200] [dec:h264 @ 000001c3cee25980] Decoder thread received EOF packet
[h264 @ 000001c3d1723e80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f0e80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[vist#0:0/h264 @ 000001c3cee12200] [dec:h264 @ 000001c3cee25980] Decoder returned EOF, finishing
[h264 @ 000001c3d20f15c0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[vist#0:0/h264 @ 000001c3cee12200] [dec:h264 @ 000001c3cee25980] Terminating thread with return code 0 (success)
[h264 @ 000001c3d20f3340] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f4200] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f1240] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f3ac0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f1980] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f1d40] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f2100] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f3700] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f2480] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080] EOF while reading input
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080] Terminating thread with return code 0 (success)
[h264 @ 000001c3d20f2840] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1031940] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d1032080] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[AVFilterGraph @ 000001c3d3b55e40] Setting 'model' to value 'path=D\:/Patric/MinaDokument/GitHub/vmaf/model/vmaf_float_v0.6.1.json'
[AVFilterGraph @ 000001c3d3b55e40] Setting 'log_path' to value 'D\:/Patric/ffmpeg/vmaf_log.json'
[AVFilterGraph @ 000001c3d3b55e40] Setting 'log_fmt' to value 'json'
[h264 @ 000001c3d1030a80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d10311c0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f0e80] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[h264 @ 000001c3d20f15c0] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f3340] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 2
[h264 @ 000001c3d20f4200] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
[vist#1:0/h264 @ 000001c3cee257c0] [dec:h264 @ 000001c3d1cf9a80] Decoder thread received EOF packet
[h264 @ 000001c3d20f1240] nal_unit_type: 1(Coded slice of a non-IDR picture), nal_ref_idc: 0
libvmaf DEBUG feature extractor "float_adm" registered with 0 opts
libvmaf DEBUG feature extractor "float_motion" registered with 0 opts
libvmaf DEBUG feature extractor "float_vif" registered with 0 opts
[graph 0 input from stream 0:0 @ 000001c3cedbaec0] w:414 h:420 pixfmt:yuv420p tb:1/12800 fr:25/1 sar:0/1 csp:unknown range:unknown
[graph 0 input from stream 1:0 @ 000001c3cedbafc0] w:414 h:420 pixfmt:yuv420p tb:1/12800 fr:25/1 sar:0/1 csp:unknown range:unknown
[AVFilterGraph @ 000001c3d3b55e40] query_formats: 4 queried, 9 merged, 0 already done, 0 delayed
[Parsed_libvmaf_0 @ 000001c3cedbb300] [framesync @ 000001c3cedbadc8] Selected 1/12800 time base
[Parsed_libvmaf_0 @ 000001c3cedbb300] [framesync @ 000001c3cedbadc8] Sync level 2
[graph 0 input from stream 0:0 @ 000001c3cedbaec0] video frame properties congruent with link at pts_time: 0
[graph 0 input from stream 1:0 @ 000001c3cedbafc0] video frame properties congruent with link at pts_time: 0
Output #0, null, to 'pipe:':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf61.9.106
  Stream #0:0, 0, 1/25: Video: wrapped_avframe, 1 reference frame, yuv420p(progressive, left), 414x420, 0/1, q=2-31, 200 kb/s, 25 fps, 25 tbn
    Metadata:
      encoder         : Lavc61.31.101 wrapped_avframe
[out#0/null @ 000001c3cedba740] Starting thread...
[vist#1:0/h264 @ 000001c3cee257c0] [dec:h264 @ 000001c3d1cf9a80] Decoder returned EOF, finishing
[vist#1:0/h264 @ 000001c3cee257c0] [dec:h264 @ 000001c3d1cf9a80] Terminating thread with return code 0 (success)
[Parsed_libvmaf_0 @ 000001c3cedbb300] [framesync @ 000001c3cedbadc8] Sync level 1
[Parsed_libvmaf_0 @ 000001c3cedbb300] [framesync @ 000001c3cedbadc8] Sync level 0
[out_#0:0 @ 000001c3cedb9a80] EOF on sink link out_#0:0:default.
[fc#0 @ 000001c3cedd9bc0] Filtergraph returned EOF, finishing
[fc#0 @ 000001c3cedd9bc0] All consumers returned EOF
[vost#0:0/wrapped_avframe @ 000001c3cee22c40] [enc:wrapped_avframe @ 000001c3cee16400] Encoder thread received EOF
[Parsed_libvmaf_0 @ 000001c3cedbb300] VMAF score: 51.427112
[vost#0:0/wrapped_avframe @ 000001c3cee22c40] Terminating thread with return code 0 (success)
cou[out#0/null @ 000001c3cedba740] ldAll streams finished
 n[out#0/null @ 000001c3cedba740] otTerminating thread with return code 0 (success)
 open file: D\:/Patric/ffmpeg/vmaf_log.json
[fc#0 @ 000001c3cedd9bc0] Terminating thread with return code 0 (success)
[out#0/null @ 000001c3cedba740] Output file #0 (pipe:):
[out#0/null @ 000001c3cedba740]   Output stream #0:0 (video): 25 frames encoded; 25 packets muxed (11000 bytes);
[out#0/null @ 000001c3cedba740]   Total: 25 packets (11000 bytes) muxed
[out#0/null @ 000001c3cedba740] video:11KiB audio:0KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: unknown
frame=   25 fps=0.0 q=-0.0 Lsize=N/A time=00:00:01.00 bitrate=N/A speed=4.36x
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80] Input file #0 (D:/Patric/ffmpeg/quantized_video.mp4):
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80]   Input stream #0:0 (video): 25 packets read (15572 bytes); 25 frames decoded; 0 decode errors;
[in#0/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3ced4eb80]   Total: 25 packets (15572 bytes) demuxed
[AVIOContext @ 000001c3cee17ec0] Statistics: 16730 bytes read, 0 seeks
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080] Input file #1 (D:/Patric/ffmpeg/original_video.mp4):
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080]   Input stream #1:0 (video): 25 packets read (18135 bytes); 25 frames decoded; 0 decode errors;
[in#1/mov,mp4,m4a,3gp,3g2,mj2 @ 000001c3cedd8080]   Total: 25 packets (18135 bytes) demuxed
[AVIOContext @ 000001c3cee18180] Statistics: 19293 bytes read, 0 seeks
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageFilter

def main() -> None:
  target_width = 1920
  target_height = 1080
  blur_ratio = 4.0

  cwd = Path().cwd()
  src_dir = cwd.joinpath('img/0-preprocessed')
  dst_dir = cwd.joinpath('img/1-postprocessed')
  log_dir = cwd.joinpath('log/')

  if not src_dir.is_dir():
    src_dir.mkdir()

  if not dst_dir.is_dir():
    dst_dir.mkdir()

  if not log_dir.is_dir():
    log_dir.mkdir()

  current_time = datetime.now().strftime('%Y%m%d%H%M%S')
  log_path = log_dir.joinpath(f'{current_time}').with_suffix('.log')

  # 先に最大拡大率を計算しておく
  max_resize_ratio = 0.0
  for src_path in src_dir.glob('*.png'):
    with Image.open(src_path) as img:
      src_w, src_h = img.size
      resize_ratio = max(target_width / src_w, target_height / src_h)
      max_resize_ratio = max(resize_ratio, max_resize_ratio)

  blur_radius = max_resize_ratio * blur_ratio
  processed_file_counter = 0

  with log_path.open('+w', encoding='utf-8') as log_file:
    def log_output(log: str = '') -> None:
      print(log)
      log_file.write(log + '\n')

    log_output(f'target_size: {target_width} x {target_height}')
    log_output(f'blur_ratio: {blur_ratio}')
    log_output(f'max_resize_ratio: {max_resize_ratio}')
    log_output(f'blur_radius: {blur_radius}')
    log_output()

    for src_path in src_dir.glob('*.png'):
      with Image.open(src_path) as img:
        filename = src_path.name

        src_w, src_h = img.size
        resize_ratio = max(target_width / src_w, target_height / src_h)
        dst_w, dst_h = (int(src_w * resize_ratio), int(src_h * resize_ratio))

        # LANCZOSが多分一番きれい
        resized = img.resize(
          size=(dst_w, dst_h),
          resample=Image.Resampling.LANCZOS,
        )

        blurred = resized.filter(ImageFilter.GaussianBlur(blur_radius))

        log_output(f'{filename}: resize_ratio = {resize_ratio}, size: {src_w} x {src_h} -> {dst_w} x {dst_h}')

        dst_path = dst_dir.joinpath(filename)
        blurred.save(dst_path)

        processed_file_counter += 1

    log_output()
    log_output(f'processed {processed_file_counter} file' + ('.' if processed_file_counter == 1 else 's.'))

if __name__ == '__main__':
  main()

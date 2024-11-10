This is an open source GIS package. There are many useful tools in it.
1.NC文件批量转换TIF工具

## 功能描述
该工具用于批量将.nc（NetCDF）文件转换为GeoTIFF格式。主要功能包括：
- 批量处理整个文件夹中的.nc文件
- 自动为每个.nc文件创建独立的输出文件夹
- 保留地理参考信息
- 将.nc文件中的每个变量分别转换为独立的GeoTIFF文件

## 注意事项
1. 确保.nc文件包含有效的经纬度信息
2. 确保有足够的磁盘空间存储输出文件
3. 处理大文件时可能需要较长时间
4. 建议先处理少量文件进行测试

## 错误处理
- 脚本会跳过处理出错的文件并继续处理其他文件
- 错误信息会被打印到控制台
- 常见错误包括：
  - 文件读取错误
  - 内存不足
  - 输出路径权限问题

2.MODIS数据批处理工具

这是一个用于批量处理MODIS HDF数据的Python工具，可以将MODIS HDF数据转换为GeoTIFF格式，并支持投影转换功能。

## 功能特点

- 批量处理MODIS HDF文件
- 支持转换为GeoTIFF格式
- 可自定义输出投影坐标系
- 支持选择性波段提取
- 保持地理参考信息
- 详细的进度显示和错误处理

### 基本用法

```python
from modis_processor import process_with_error_handling

# 基本批量转换
process_with_error_handling(
    input_directory="path/to/input",
    output_directory="path/to/output"
)
```

### 高级用法

```python
# 指定投影和波段的转换
process_with_error_handling(
    input_directory="path/to/input",
    output_directory="path/to/output",
    target_epsg=4326,  # WGS84投影
    selected_bands=[0, 1]  # 只处理第1和第2波段
)
```

## 参数说明

### process_with_error_handling函数

| 参数 | 类型 | 说明 | 默认值 |
|------|------|------|--------|
| input_directory | str | 输入文件夹路径 | 必填 |
| output_directory | str | 输出文件夹路径 | 必填 |
| target_epsg | int | 目标投影的EPSG代码 | None |
| selected_bands | list | 需要提取的波段列表 | None |

## 常见投影代码参考

| EPSG代码 | 说明 |
|----------|------|
| 4326 | WGS84地理坐标系 |
| 3857 | Web墨卡托投影 |
| 32650 | WGS84 UTM 50N |
| 32649 | WGS84 UTM 49N |

## 输出文件说明

输出文件将按以下格式命名：
```
原文件名_band_波段序号.tif
```

例如：
```
MOD09GA.A2020001.h27v05_band_0.tif
```

## 注意事项

1. 数据准备
   - 确保MODIS数据文件格式正确
   - 检查输入文件的完整性

2. 存储空间
   - 确保有足够的磁盘空间
   - GeoTIFF文件可能比原HDF文件大

3. 处理时间
   - 大文件处理可能需要较长时间
   - 投影转换会增加处理时间

4. 错误处理
   - 程序会跳过处理失败的文件
   - 错误信息会被记录并显示

## 常见问题解决

1. 无法找到HDF文件
   - 检查输入路径是否正确
   - 确认文件扩展名是否为.hdf

2. 内存错误
   - 减少同时处理的波段数量
   - 确保系统有足够的可用内存

3. 投影转换失败
   - 检查EPSG代码是否正确
   - 确认原数据的投影信息完整
# 6. 字典

[TOC]

## 前言及介绍

字典可以为真实物体建模. 
如可以创建一个人的字典: 姓名/年龄/地址/职业
还可以创建任意两种相关的信息: 一系列山脉和海拔.

## 使用字典

```python
alien_0 = {'color': 'green', 'points': 5}
new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")
```

### 添加键值对

字典是动态结构, 可以随时在其中添加键值对.

> 屏幕坐标系的原点通常为**左上角**
> 屏幕左边缘, 离屏幕上边缘25像素的坐标为: (0, 25)

有时候, 需要在空字典中添加键值对. 

```python
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)
```

### 删除键值对

- `del`删除. 如`del alien_0['points']`

## 遍历词典

可以写准确的key, value的名称, 更方便理解. 如: `for name, language in favorite_languages.items()`

### 遍历key

`for k in favorite_languages.keys(): ...` 等价于 `for k in favorite_languages` (默认遍历字典的key)

### 按顺序便利key

`for k in sorted(favorite_languages.keys())`

### 遍历value
方法: `values()`
集合: `for language in set(favorite_languages.values())`

## 嵌套

- 列表中嵌套字典
- 字典中嵌套列表
- 字典中嵌套字典

### 字典列表

```python
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}

aliens = [alien_0, alien_1]

for alien in aliens:
    print(alien)
```

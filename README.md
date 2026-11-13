# LeetCode (Python)

每道题是一个 **独立可运行的 Python 脚本 + 一个 pytest 测试**。

## 目录结构

```
problems/
  0001_two_sum/
    two_sum.py            # 题解，可直接 python 运行
    test_two_sum.py       # 测试
  0206_reverse_linked_list/
    reverse_linked_list.py
    test_reverse_linked_list.py
common/                   # 公共数据结构：ListNode / TreeNode 及构造、序列化工具
scripts/new.py            # 新建题目脚手架
tests/                    # common 的测试
```

命名规则：`problems/<4位题号>_<slug下划线>/<slug下划线>.py`，测试文件为 `test_<同名>.py`。
slug 以数字开头时（如 `3sum`）自动加前缀 `p` → `p3sum.py`。
模块名直接用题目 slug，全局唯一，所以不同题目的测试不会互相冲突。

## 使用

```bash
pip install -r requirements.txt

# 新建一道题（slug 取自 leetcode.com/problems/<slug>/）
python scripts/new.py 15 3sum
python scripts/new.py 104 maximum-depth-of-binary-tree

# 直接运行某道题
python problems/0001_two_sum/two_sum.py

# 测试
pytest                                  # 全部
pytest problems/0001_two_sum            # 单题
pytest -k reverse                       # 按名字过滤
```

## 约定

- 题解文件顶部 docstring 写：题号标题、链接、难度、标签、思路、复杂度。
- 保留 LeetCode 原始的 `class Solution` 方法签名，方便直接复制提交。
- 需要链表 / 二叉树时从 `common` 导入 `ListNode`、`TreeNode`、`build_list`、`build_tree` 等；
  模板里已带好把仓库根目录加入 `sys.path` 的一行，脚本单独运行也能 import。
- 不需要 `common` 的题，可以删掉模板里的 `sys.path` 和 import 两行。

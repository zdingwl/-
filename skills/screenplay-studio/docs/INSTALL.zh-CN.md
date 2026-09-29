# Screenplay Studio 安装与打包

## 最重要的一点

不要把整个 GitHub 仓库作为一个 Skill 安装。

仓库里包含多套独立 Skill，因此仓库根目录下会存在多个 `SKILL.md`。

Screenplay Studio 的实际 Skill 根目录是：

~~~text
skills/screenplay-studio/
~~~

安装或打包时，只处理这个目录。

## 目录要求

可安装包应只有一个顶层文件夹：

~~~text
screenplay-studio/
├── SKILL.md
├── references/
├── workflows/
├── templates/
├── scripts/
├── docs/
├── examples/
└── evaluations/
~~~

其中必须只有一个 `SKILL.md`。

## 生成 ZIP

在仓库根目录运行：

~~~bash
python skills/screenplay-studio/scripts/package_skill.py
~~~

默认输出：

~~~text
dist/screenplay-studio-2.0.0.zip
~~~

ZIP 内部结构为：

~~~text
screenplay-studio/
  SKILL.md
  ...
~~~

不会把 `skills/`、仓库根 README 或其他 Skill 一起打进去。

## 自定义输出位置

~~~bash
python skills/screenplay-studio/scripts/package_skill.py \
  --output /tmp/screenplay-studio.zip
~~~

## 打包前验证

~~~bash
python skills/screenplay-studio/scripts/validate_skill.py
~~~

验证包括：

- 唯一 `SKILL.md`
- front matter 中的 name / description
- 主文件引用路径存在
- Level 2 正好 120 个知识点
- 1–120 无缺号、无重复
- 单文件大小与文件数量处于 Skill bundle 限制内

## ChatGPT / Agent Skills

安装时使用 `screenplay-studio/` 目录或由上述脚本生成的 ZIP。

Skill 被发现时首先依赖 `name` 与 `description` 判断是否相关；真正执行后再按
`SKILL.md` 中的加载地图读取 references、workflows 和模板。

## API 上传注意

使用 ZIP 上传时，ZIP 必须包含单一顶层 Skill 目录，而不是把多个 Skill 打在同一个 bundle 里。

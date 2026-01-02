
# 🧩 .dotfiles

> Personal configuration files for my Linux setup — curated, broken, fixed, and refined over time.

## What are dotfiles?

**Dotfiles** are plain-text configuration files used by Unix-like systems (Linux, BSD, macOS) to control the behavior of shells, editors, terminals, window managers, and many system tools.  
They usually start with a dot (`.`), which is why they’re hidden by default.

This repository is my **living record of how I configure and understand my system** — not a polished template, but an honest, evolving setup shaped by daily use, experimentation, and occasional breakage.

---

## 🧠 Philosophy

- 🔗 Configs are managed using **Git + symlinks**
- 📁 Real files live inside this repository
- 🧪 Changes are made to learn, not just to customize
- ♻️ Everything is reproducible on a new machine
- 🔐 No secrets, no cache, no system-generated junk

If something exists here, it’s because I use it — or I wanted to understand it.

---

## 🛠️ What’s inside

This repository may include configurations for:

### 🖥️ Terminal
- Alacritty
- Kitty (if/when used)

### 🐚 Shell
- Bash / Zsh
- Aliases, functions, environment variables
- Prompt customization

### ✍️ Editor
- Neovim / Vim configuration
- Language and workflow experiments

### 🪟 Desktop / Window Management
- GNOME / KDE / XFCE / i3  
  (depends on the phase of life and hardware)

### 🧰 CLI Tools
- git
- tmux
- starship
- fzf, ripgrep, and related utilities

### ⚙️ System-level configs
- `.profile`, `.bashrc`, `.zshrc`
- X11 / Wayland tweaks (where applicable)

Not everything is always stable.  
Some configurations exist purely because I wanted to understand *how they work*.

---

## 📂 Repository structure (example)

```text
.dotfiles/
├── alacritty/
│   └── alacritty.yml
├── nvim/
│   └── init.lua
├── bash/
│   ├── bashrc
│   └── aliases
├── git/
│   └── gitconfig
├── tmux/
│   └── tmux.conf
└── README.md
````

The exact structure may change over time as tools are added, removed, or replaced.

---

## 🔗 How these files are used

Applications expect configs in standard locations like:

```
~/.bashrc
~/.config/alacritty/
~/.config/nvim/
```

Instead of copying files, this repo uses **symbolic links** so that:

* Git tracks only the real files
* The system continues to work normally
* One source of truth is maintained

---

## 🚧 Status

This is an **actively evolving setup**.

Things may be:

* refactored
* rewritten
* replaced
* removed entirely

That’s intentional.

---

## 📜 License

Personal use.
Feel free to read, learn, and borrow ideas — but expect opinions.





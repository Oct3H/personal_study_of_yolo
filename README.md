**个人学习用，小练习<br>**
---------
没啥价值，不用管<br>
images_文件夹没上传<br>
用了老版本yolo，新版本每次都要联网，需要🪜




<br>
<br>
- YOLO may produce low-confidence false positives
- Tracking ID may persist across frames
- Event logic is currently rule-based




<br>
<br>
<br>
<br>
<br>
<br>
“为什么会出现羊叫？”<br>
│<br>
├── Event？<br>
│   └── ❌ 排除<br>
│<br>
├── Analyzer？<br>
│   └── 暂时排除<br>
│<br>
├── Track？<br>
│   └── ❌ 排除<br>
│<br>
└── YOLO Detection<br>
    │<br>
    └── ✅ 已确认这里出现 sheep<br>
         │<br>
         ├── 低置信度误检 ← 目前最大嫌疑<br>
         ├── conf 阈值<br>
         ├── 模型本身识别能力<br>
         ├── 视频帧/姿态/遮挡<br>
         └── 数据集类别边界<br>
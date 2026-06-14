import streamlit as st

st.set_page_config(
    page_title="تصور مشروع الأتمتة",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;900&display=swap');

* { font-family: 'Cairo', sans-serif !important; }

html, body, [class*="css"] {
    direction: rtl;
    text-align: right;
}

.stApp {
    background: linear-gradient(135deg, #0a0a1a 0%, #0f1535 50%, #0a0a1a 100%);
    color: #e8eaf6;
}

/* Hero */
.hero {
    text-align: center;
    padding: 60px 20px 40px;
}
.hero-badge {
    display: inline-block;
    background: rgba(99,102,241,0.15);
    border: 1px solid rgba(99,102,241,0.4);
    color: #a5b4fc;
    padding: 6px 18px;
    border-radius: 20px;
    font-size: 13px;
    margin-bottom: 20px;
    letter-spacing: 1px;
}
.hero h1 {
    font-size: 2.8rem;
    font-weight: 900;
    color: #fff;
    line-height: 1.3;
    margin-bottom: 16px;
}
.hero h1 span {
    background: linear-gradient(90deg, #6366f1, #8b5cf6, #a78bfa);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero p {
    font-size: 1.1rem;
    color: #94a3b8;
    max-width: 600px;
    margin: 0 auto;
    line-height: 1.8;
}

/* Cards */
.card {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 28px;
    margin-bottom: 20px;
    transition: border-color 0.3s;
}
.card:hover { border-color: rgba(99,102,241,0.4); }

.card-title {
    font-size: 1.1rem;
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
}

/* Stats */
.stat-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    margin: 30px 0;
}
.stat-item {
    background: rgba(99,102,241,0.08);
    border: 1px solid rgba(99,102,241,0.2);
    border-radius: 12px;
    padding: 20px;
    text-align: center;
}
.stat-num {
    font-size: 2rem;
    font-weight: 900;
    color: #a5b4fc;
    display: block;
}
.stat-label {
    font-size: 0.85rem;
    color: #64748b;
    margin-top: 4px;
}

/* Flow */
.flow-step {
    display: flex;
    align-items: flex-start;
    gap: 16px;
    margin-bottom: 16px;
}
.step-num {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    font-size: 14px;
    flex-shrink: 0;
}
.step-content { flex: 1; }
.step-title {
    font-weight: 700;
    color: #e2e8f0;
    font-size: 0.95rem;
}
.step-desc {
    color: #64748b;
    font-size: 0.85rem;
    margin-top: 4px;
}

/* Compare table */
.compare-row {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    gap: 12px;
    margin-bottom: 10px;
    align-items: center;
}
.compare-label { color: #94a3b8; font-size: 0.9rem; }
.compare-bad {
    background: rgba(239,68,68,0.1);
    border: 1px solid rgba(239,68,68,0.2);
    color: #fca5a5;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 0.85rem;
    text-align: center;
}
.compare-good {
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.2);
    color: #86efac;
    padding: 6px 12px;
    border-radius: 8px;
    font-size: 0.85rem;
    text-align: center;
}

/* Deliverables */
.deliverable-item {
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 12px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
}
.deliverable-item:last-child { border-bottom: none; }
.deliverable-icon {
    font-size: 1.4rem;
    width: 40px;
    text-align: center;
}
.deliverable-text { flex: 1; }
.deliverable-name {
    font-weight: 600;
    color: #e2e8f0;
    font-size: 0.95rem;
}
.deliverable-desc {
    color: #64748b;
    font-size: 0.8rem;
    margin-top: 2px;
}

/* Timeline */
.timeline-item {
    display: flex;
    gap: 16px;
    margin-bottom: 20px;
    position: relative;
}
.timeline-week {
    background: linear-gradient(135deg, #6366f1, #8b5cf6);
    color: white;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 700;
    white-space: nowrap;
    height: fit-content;
    margin-top: 2px;
}
.timeline-content { flex: 1; }
.timeline-title {
    font-weight: 700;
    color: #e2e8f0;
    margin-bottom: 6px;
}
.timeline-tasks { color: #64748b; font-size: 0.85rem; line-height: 1.8; }

/* Question section */
.question-section {
    background: linear-gradient(135deg, rgba(99,102,241,0.1), rgba(139,92,246,0.1));
    border: 1px solid rgba(99,102,241,0.3);
    border-radius: 16px;
    padding: 32px;
    margin: 30px 0;
    text-align: center;
}
.question-section h3 {
    color: #a5b4fc;
    font-size: 1.3rem;
    font-weight: 700;
    margin-bottom: 8px;
}
.question-section p {
    color: #64748b;
    font-size: 0.9rem;
    margin-bottom: 24px;
}

/* Radio custom */
.stRadio > label { color: #94a3b8 !important; }
.stRadio [data-testid="stMarkdownContainer"] p { color: #e2e8f0 !important; }

/* Buttons */
.stButton > button {
    background: linear-gradient(135deg, #6366f1, #8b5cf6) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    padding: 12px 32px !important;
    font-family: 'Cairo', sans-serif !important;
    font-weight: 700 !important;
    font-size: 1rem !important;
    width: 100%;
    transition: opacity 0.2s !important;
}
.stButton > button:hover { opacity: 0.85 !important; }

/* Section header */
.section-header {
    font-size: 1.4rem;
    font-weight: 800;
    color: #e2e8f0;
    margin: 40px 0 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid rgba(99,102,241,0.3);
}

/* Result card */
.result-card {
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.25);
    border-radius: 16px;
    padding: 28px;
    margin-top: 20px;
}
.result-card h3 { color: #86efac; font-size: 1.1rem; margin-bottom: 16px; }

.tag {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: 600;
    margin: 4px;
}
.tag-blue { background: rgba(99,102,241,0.15); color: #a5b4fc; border: 1px solid rgba(99,102,241,0.3); }
.tag-purple { background: rgba(139,92,246,0.15); color: #c4b5fd; border: 1px solid rgba(139,92,246,0.3); }
.tag-green { background: rgba(34,197,94,0.15); color: #86efac; border: 1px solid rgba(34,197,94,0.3); }

hr { border-color: rgba(255,255,255,0.08) !important; }

</style>
""", unsafe_allow_html=True)

# ── HERO ──────────────────────────────────────────────
st.markdown("""
<div class="hero">
    <h1>نظام أتمتة<br><span>دراسات الجدوى وخطط العمل</span></h1>
    <p>من فكرة العميل إلى ملفات جاهزة في دقائق — بدون تدخل يدوي</p>
</div>
""", unsafe_allow_html=True)

# ── STATS ──────────────────────────────────────────────
st.markdown("""
<div class="stat-grid">
    <div class="stat-item">
        <span class="stat-num">5 دقائق</span>
        <div class="stat-label">بدل 3-5 ساعات يدوي</div>
    </div>
    <div class="stat-item">
        <span class="stat-num">صفر</span>
        <div class="stat-label">تدخل بشري في الإنتاج</div>
    </div>
    <div class="stat-item">
        <span class="stat-num">∞</span>
        <div class="stat-label">مشاريع بالتوازي</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── HOW IT WORKS ──────────────────────────────────────────────
st.markdown('<div class="section-header">⚙️ كيف يشتغل النظام</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">📥 مثال عملي</div>
        <div style="background:rgba(0,0,0,0.3);border-radius:10px;padding:16px;font-family:monospace;font-size:0.85rem;color:#94a3b8;line-height:2;">
            العميل يكتب:<br>
            <span style="color:#a5b4fc;">"مغسلة سيارات متنقلة، رأس مال 50,000 جنيه، القاهرة"</span><br><br>
            ↓<br><br>
            النظام أوتوماتيك:<br>
            <span style="color:#86efac;">✅ بحث شامل عن السوق<br>
            ✅ دراسة جدوى كاملة<br>
            ✅ نموذج العمل التجاري<br>
            ✅ خطة التسويق والإعلانات</span><br><br>
            <span style="color:#fbbf24;">📄 ملفات Word/Excel جاهزة</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">🔄 خطوات التنفيذ</div>
    """, unsafe_allow_html=True)

    steps = [
        ("استقبال بيانات المشروع", "من تيليجرام أو موقع ويب"),
        ("سحب النموذج المناسب", "من قاعدة RAG الذكية"),
        ("إرسال لـ DeepSeek", "مع برومبت احترافي مخصص"),
        ("مراجعة النتيجة", "تلقائياً أو بمراجعة بشرية"),
        ("تسليم الملفات للعميل", "Word / Excel جاهزة"),
    ]

    for i, (title, desc) in enumerate(steps, 1):
        st.markdown(f"""
        <div class="flow-step">
            <div class="step-num">{i}</div>
            <div class="step-content">
                <div class="step-title">{title}</div>
                <div class="step-desc">{desc}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

# ── DELIVERABLES ──────────────────────────────────────────────
st.markdown('<div class="section-header">📂 المخرجات لكل مشروع</div>', unsafe_allow_html=True)

deliverables = [
    ("📄", "بحث شامل", "السوق، المنافسين، الموردين، المخاطر، الفرص"),
    ("📊", "دراسة الجدوى", "تكاليف، عوائد، نقطة التعادل، التحليل المالي"),
    ("💼", "نموذج العمل التجاري", "Business Model Canvas مخصص للمشروع"),
    ("📋", "خطة العمل", "خطوات التنفيذ، الأولويات، الجداول الزمنية"),
    ("📣", "خطة التسويق", "Hook، CTA، إعلانات، ميزانية، KPIs"),
]

st.markdown('<div class="card">', unsafe_allow_html=True)
for icon, name, desc in deliverables:
    st.markdown(f"""
    <div class="deliverable-item">
        <div class="deliverable-icon">{icon}</div>
        <div class="deliverable-text">
            <div class="deliverable-name">{name}</div>
            <div class="deliverable-desc">{desc}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── COMPARISON ──────────────────────────────────────────────
st.markdown('<div class="section-header">📊 قبل وبعد النظام</div>', unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <div class="compare-row">
        <div class="compare-label" style="font-weight:700;color:#e2e8f0;">المعيار</div>
        <div style="text-align:center;font-weight:700;color:#fca5a5;">قبل (يدوي)</div>
        <div style="text-align:center;font-weight:700;color:#86efac;">بعد (النظام)</div>
    </div>
    <div class="compare-row">
        <div class="compare-label">⏱️ وقت المشروع</div>
        <div class="compare-bad">3 – 5 ساعات</div>
        <div class="compare-good">5 دقائق</div>
    </div>
    <div class="compare-row">
        <div class="compare-label">🔁 تدخل بشري</div>
        <div class="compare-bad">في كل خطوة</div>
        <div class="compare-good">صفر</div>
    </div>
    <div class="compare-row">
        <div class="compare-label">📈 مشاريع/يوم</div>
        <div class="compare-bad">1 – 2 مشاريع</div>
        <div class="compare-good">غير محدود</div>
    </div>
    <div class="compare-row">
        <div class="compare-label">✅ اتساق الجودة</div>
        <div class="compare-bad">متغير</div>
        <div class="compare-good">ثابت وموحد</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ── TECH STACK ──────────────────────────────────────────────
st.markdown('<div class="section-header">🛠️ المكونات التقنية</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="card">
        <div class="card-title">🧠 الذكاء الاصطناعي</div>
        <span class="tag tag-blue">DeepSeek</span>
        <span class="tag tag-purple">RAG System</span>
        <span class="tag tag-blue">LangChain</span>
        <span class="tag tag-purple">Vector DB</span>
        <div style="color:#64748b;font-size:0.85rem;margin-top:12px;">النماذج والقوالب تتحول لقاعدة بيانات ذكية يفهمها الـ AI</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <div class="card-title">⚡ الأتمتة والتحكم</div>
        <span class="tag tag-green">Hermes</span>
        <span class="tag tag-blue">Telegram Bot</span>
        <span class="tag tag-purple">Web Dashboard</span>
        <div style="color:#64748b;font-size:0.85rem;margin-top:12px;">بتتحكم في النظام من تيليجرام أو موقع ويب بكل سهولة</div>
    </div>
    """, unsafe_allow_html=True)

# ── TIMELINE ──────────────────────────────────────────────
st.markdown('<div class="section-header">🗓️ خطة التنفيذ</div>', unsafe_allow_html=True)

timeline = [
    ("أسبوع 1", "إعداد قاعدة RAG", "• رفع جميع النماذج\n• تحويلها لـ Embeddings\n• اختبار الاسترجاع"),
    ("أسبوع 1-2", "ربط DeepSeek", "• بناء البرومبتات الاحترافية\n• اختبار جودة المخرجات\n• ضبط النتائج"),
    ("أسبوع 2-3", "واجهة التحكم", "• بناء تيليجرام بوت أو موقع ويب\n• تصميم تجربة المستخدم"),
    ("أسبوع 3", "أتمتة Hermes", "• ربط جميع المكونات\n• أتمتة الـ Workflow كاملاً"),
    ("أسبوع 4", "اختبار وتسليم", "• اختبار شامل\n• تعديلات وتحسينات\n• تسليم النظام"),
]

st.markdown('<div class="card">', unsafe_allow_html=True)
for week, title, tasks in timeline:
    st.markdown(f"""
    <div class="timeline-item">
        <div class="timeline-week">{week}</div>
        <div class="timeline-content">
            <div class="timeline-title">{title}</div>
            <div class="timeline-tasks">{tasks.replace(chr(10), '<br>')}</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ── CLIENT QUESTION ──────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div class="question-section">
    <h3>سؤال مهم قبل نبدأ 🤔</h3>
    <p>عشان نحدد التقنيات والبنية التحتية المناسبة</p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns([1,2,1])
with col2:
    use_type = st.radio(
        "**النظام ده هيكون للاستخدام في:**",
        options=[
            "🏢 Production — لخدمة عملاء فعليين بشكل يومي",
            "👤 مشروع شخصي — لتسريع شغلي الخاص بس",
        ],
        index=None,
        key="use_type"
    )

    if use_type:
        submitted = st.button("تأكيد الاختيار ✅")

        if submitted:
            if "Production" in use_type:
                st.markdown("""
                <div class="result-card">
                    <h3>✅ ممتاز — اخترت Production</h3>
                    <div style="color:#94a3b8;line-height:2;font-size:0.9rem;">
                        هنحتاج نركز على:<br>
                        🔒 <strong style="color:#e2e8f0;">الأمان وعزل بيانات العملاء</strong><br>
                        ⚡ <strong style="color:#e2e8f0;">سرعة الاستجابة تحت الضغط</strong><br>
                        📈 <strong style="color:#e2e8f0;">Scalability للتوسع مستقبلاً</strong><br>
                        🖥️ <strong style="color:#e2e8f0;">سيرفر VPS مخصص أو Cloud</strong><br>
                        📊 <strong style="color:#e2e8f0;">لوحة تحكم لمتابعة المشاريع</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown("""
                <div class="result-card">
                    <h3>✅ تمام — مشروع شخصي</h3>
                    <div style="color:#94a3b8;line-height:2;font-size:0.9rem;">
                        نقدر نبدأ بشكل أخف وأسرع:<br>
                        💻 <strong style="color:#e2e8f0;">تشغيل محلي على جهازك</strong><br>
                        🤖 <strong style="color:#e2e8f0;"> Sreamlit app زي اللى حضرتك شايفه  </strong><br>
                        💸 <strong style="color:#e2e8f0;">تكلفة أقل بكتير</strong><br>
                        🚀 <strong style="color:#e2e8f0;">وقت تنفيذ أسرع</strong><br>
                        🔄 <strong style="color:#e2e8f0;">ممكن نطوره لـ Production بعدين</strong>
                    </div>
                </div>
                """, unsafe_allow_html=True)

# ── FOOTER ──────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style="text-align:center;color:#334155;font-size:0.8rem;padding:20px 0;">
    جاهز نبدأ؟ رد على السؤال وهنحدد أفضل مسار للتنفيذ 🚀
</div>
""", unsafe_allow_html=True)

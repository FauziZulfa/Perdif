import streamlit as st
import sympy as sp
import random

# ════════════════════════════════════════════════════════════
# KONFIGURASI HALAMAN
# ════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="PD Homogen | Kelompok 2",
    page_icon="🧮",
    layout="centered"
)

# ════════════════════════════════════════════════════════════
# CSS KUSTOM
# ════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Source+Code+Pro:wght@400;600&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.header-box {
    background: linear-gradient(135deg, #1a2f4e 0%, #2563eb 100%);
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    color: white;
    margin-bottom: 28px;
}

.header-box h1 {
    font-family: 'Playfair Display', serif;
    font-size: 2.2rem;
    margin: 0 0 6px 0;
}

.header-box p {
    margin: 0;
    opacity: 0.8;
    font-size: 0.95rem;
}

.info-box {
    background: #dbeafe;
    border-left: 4px solid #2563eb;
    border-radius: 0 8px 8px 0;
    padding: 10px 14px;
    font-size: 0.88rem;
    color: #1a2f4e;
    margin-bottom: 12px;
}

.hasil-sukses {
    background: #dcfce7;
    border: 1px solid #16a34a;
    border-left: 4px solid #16a34a;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    font-family: 'Source Code Pro', monospace;
    font-size: 0.95rem;
    color: #14532d;
    line-height: 1.8;
}

.hasil-gagal {
    background: #fee2e2;
    border: 1px solid #dc2626;
    border-left: 4px solid #dc2626;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    font-family: 'Source Code Pro', monospace;
    font-size: 0.95rem;
    color: #7f1d1d;
    white-space: pre-wrap;
}

.hasil-peringatan {
    background: #fef9c3;
    border: 1px solid #ca8a04;
    border-left: 4px solid #ca8a04;
    border-radius: 0 8px 8px 0;
    padding: 14px 18px;
    font-size: 0.9rem;
    color: #713f12;
}

.langkah-judul {
    background: #1a2f4e;
    color: white;
    padding: 10px 16px;
    border-radius: 8px 8px 0 0;
    font-weight: 600;
    font-size: 0.9rem;
}

.langkah-isi {
    background: #f8fafc;
    border: 1px solid #e2e8f0;
    border-top: none;
    padding: 14px 16px;
    border-radius: 0 0 8px 8px;
    font-family: 'Source Code Pro', monospace;
    font-size: 0.88rem;
    line-height: 1.7;
    margin-bottom: 12px;
    min-height: 40px;
}

.soal-box {
    background: #1a2f4e;
    color: white;
    border-radius: 10px;
    padding: 22px;
    text-align: center;
    font-family: 'Source Code Pro', monospace;
    font-size: 1.2rem;
    letter-spacing: 0.5px;
    margin-bottom: 16px;
}

.skor-box {
    background: linear-gradient(135deg, #dbeafe, white);
    border: 1px solid #2563eb;
    border-radius: 12px;
    padding: 20px;
    text-align: center;
    margin-bottom: 16px;
}

.skor-angka {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    color: #2563eb;
    line-height: 1;
}

.skor-label {
    font-size: 0.85rem;
    color: #64748b;
    margin-top: 4px;
}

.pecahan {
    display: inline-block;
    text-align: center;
    vertical-align: middle;
    margin: 0 4px;
}

.pecahan-atas {
    display: block;
    border-bottom: 2px solid currentColor;
    padding: 2px 6px;
}

.pecahan-bawah {
    display: block;
    padding: 2px 6px;
}

.solusi-box {
    background: #dcfce7;
    border: 1px solid #16a34a;
    border-left: 4px solid #16a34a;
    border-radius: 0 8px 8px 0;
    padding: 16px 20px;
    color: #14532d;
    font-size: 1rem;
    line-height: 2.2;
}

.footer {
    text-align: center;
    color: #94a3b8;
    font-size: 0.82rem;
    margin-top: 32px;
    padding-top: 16px;
    border-top: 1px solid #e2e8f0;
}
</style>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# DEFINISI VARIABEL MATEMATIKA
# ════════════════════════════════════════════════════════════
x  = sp.Symbol('x')
y  = sp.Symbol('y')
t  = sp.Symbol('t')
v  = sp.Symbol('v')
C1 = sp.Symbol('C1')

# ════════════════════════════════════════════════════════════
# FUNGSI-FUNGSI UTAMA
# ════════════════════════════════════════════════════════════

def bersihkan_input(teks):
    """Mengubah ^ menjadi ** agar bisa dibaca SymPy."""
    return teks.replace("^", "**")

def cek_homogen(ekspresi):
    """Mengecek apakah PD homogen derajat 0 atau tidak."""
    ekspresi_diganti = ekspresi.subs(x, t*x).subs(y, t*y)
    hasil = sp.simplify(ekspresi_diganti / ekspresi)
    return t not in hasil.free_symbols

def selesaikan_pd(ekspresi):
    """Mengubah ekspresi menjadi bentuk persamaan differensial untuk dsolve."""
    y_fungsi = sp.Function('y')
    ekspresi_fungsi = ekspresi.subs(y, y_fungsi(x))
    pd = sp.Eq(y_fungsi(x).diff(x), ekspresi_fungsi)
    return pd, y_fungsi

def sederhanakan(ekspresi):
    """Menyederhanakan ekspresi dengan membagi faktor persekutuan terbesar."""
    y_bersih = sp.Symbol('y')
    eks = sp.expand(ekspresi.subs(sp.Function('y')(x), y_bersih))
    faktor = sp.gcd(tuple(eks.as_coefficients_dict().values()))
    return sp.simplify(eks / faktor)

def teks_ke_html(teks):
    """Mengubah teks matematika menjadi tampilan HTML yang rapi.
    - ** menjadi superscript (pangkat atas)
    - / menjadi pecahan atas-bawah jika memungkinkan
    """
    # Ganti ** dengan superscript HTML
    # Contoh: x**2 → x<sup>2</sup>
    import re
    teks = re.sub(r'(\w+)\*\*(\d+)', r'\1<sup>\2</sup>', teks)
    return teks

def sympy_ke_html(eksp):
    """Mengubah ekspresi SymPy menjadi tampilan HTML dengan pecahan atas-bawah."""
    import re

    eksp = sp.together(eksp)   
    
    # Ambil pembilang dan penyebut
    pembilang = sp.numer(eksp)
    penyebut  = sp.denom(eksp)

    def format_bagian(bagian):
        teks = str(bagian)\
            .replace("log(", "ln(")\
            .replace("atan(", "arctan(")
    
        import re
        # Ubah pangkat dulu
        teks = re.sub(r'(\w+)\*\*(\d+)', r'\1<sup>\2</sup>', teks)
    
        # Baru ganti perkalian
        teks = teks.replace("*", "")

        return teks

    if penyebut != 1:
        # Ada penyebut → tampilkan sebagai pecahan atas-bawah
        p_html = format_bagian(pembilang)
        q_html = format_bagian(penyebut)
        return f"""<span class="pecahan">
            <span class="pecahan-atas">{p_html}</span>
            <span class="pecahan-bawah">{q_html}</span>
        </span>"""
    else:
        # Tidak ada pecahan → tampilkan biasa
        return format_bagian(pembilang)

def rapikan_solusi_html(solusi):
    """Mengubah solusi dsolve menjadi HTML dengan pecahan atas-bawah."""
    C = sp.Symbol('C')

    def proses(s):
        persamaan = s.subs(C1, C)
        c_solusi = sp.solve(persamaan, C)
        if c_solusi:
            eksp = sederhanakan(c_solusi[0])
            return f"C = {sympy_ke_html(eksp)}"
        else:
            eksp = sederhanakan(s.rhs.subs(C1, C))
            return f"y = {sympy_ke_html(eksp)}"

    if isinstance(solusi, list):
        hasil = list(dict.fromkeys([proses(s) for s in solusi]))
        return "<br>".join(hasil)
    else:
        return proses(solusi)

def rapikan_solusi_teks(solusi):
    """Versi teks biasa dari solusi (untuk pengecekan jawaban kuis)."""
    C = sp.Symbol('C')

    def proses(s):
        persamaan = s.subs(C1, C)
        c_solusi = sp.solve(persamaan, C)
        if c_solusi:
            rapi = str(sederhanakan(c_solusi[0]))\
                .replace("log(", "ln(")\
                .replace("atan(", "arctan(")\
                .replace("**", "^")
            return f"C = {rapi}"
        else:
            rapi = str(sederhanakan(s.rhs.subs(C1, C)))\
                .replace("log(", "ln(")\
                .replace("atan(", "arctan(")\
                .replace("**", "^")
            return f"y = {rapi}"

    if isinstance(solusi, list):
        hasil = list(dict.fromkeys([proses(s) for s in solusi]))
        return "\n".join(hasil)
    else:
        return proses(solusi)

def rapikan_angka(angka):
    """Membulatkan angka maksimal 3 desimal dan menghapus nol tidak perlu."""
    return f"{float(angka):.3f}".rstrip('0').rstrip('.')

def buat_langkah(ekspresi_str, ekspresi):
    langkah = []

    # Langkah 1: Tulis bentuk PD
    langkah.append(("1️⃣  Bentuk PD",
        f"dy/dx = {ekspresi_str}"))

    # Langkah 2: Uji homogenitas - tampilkan proses lengkap
    ekspresi_diganti = ekspresi.subs(x, t*x).subs(y, t*y)
    ekspresi_diganti_sederhana = sp.simplify(ekspresi_diganti)
    hasil_bagi = sp.simplify(ekspresi_diganti / ekspresi)
    
    langkah.append(("2️⃣  Uji Homogenitas",
        f"Ganti x → tx  dan  y → ty :\n\n"
        f"f(x, y)       = {ekspresi}\n\n"
        f"f(tx, ty)   = {ekspresi_diganti_sederhana}\n\n"
        f"f(tx, ty)\n"
        f"──────────── = {hasil_bagi}\n"
        f"f(x, y)\n\n"
        f"Karena variabel t hilang dari hasil pembagian,\n"
        f"maka PD ini Homogen Derajat 0"))

    # Langkah 3: Substitusi
    langkah.append(("3️⃣  Substitusi v = y/x",
        "Substitusi :\n\n"
        "  misal:   y = vx  sehingga  v = y/x  ...(1)\n\n"
        "Turunkan y = vx terhadap x :\n\n"
                    "y = vx\n\n"
        "   dy/dx = v + x dv/dx ...(2)"))

    # Langkah 4: Bentuk setelah substitusi
    ekspresi_v = sp.simplify(ekspresi.subs(y, v*x))
    ruas_kanan = sp.simplify(ekspresi_v - v)
    
    pecahan_kiri = sympy_ke_html(1/ruas_kanan)
    pecahan_kanan = sympy_ke_html(1/x)

    if ruas_kanan == 0:
        langkah.append(("4️⃣  Bentuk Setelah Substitusi",
            f"dy/dx = {sympy_ke_html(ekspresi)}\n\n"
            f"Substitusi y = vx:\n\n"
            f"v + x dv/dx = {sympy_ke_html(ekspresi_v)}\n\n"
            f"x dv/dx = 0\n\n"
            f"dv/dx = 0"
        ))
    
    else: langkah.append(("4️⃣  Bentuk Setelah Substitusi",
            f"dy/dx = {sympy_ke_html(ekspresi)}\n\n"
            f"Substitusi y = vx:\n\n"
            f"v + x dv/dx = {sympy_ke_html(ekspresi_v)}\n\n"
            f"x dv/dx = {sympy_ke_html(ekspresi_v)} - v = {sympy_ke_html(ruas_kanan)}\n\n"
            f"Pisahkan variabel x dan v :\n"
            f"   {pecahan_kiri} dv = {pecahan_kanan} dx"
    ))

    # Langkah 5: Integrasi
    integral_kiri = sp.integrate(1/ruas_kanan, v)
    integral_kanan = sp.integrate(1/x, x)

    if ruas_kanan == 0: 
        langkah.append(("5️⃣  Integralkan Kedua Ruas",
            "dv/dx = 0\n\n"
            "Integrasi:\n"
            "v = C\n\n"
            "Substitusi kembali v = y/x → y = Cx"
        ))
        
    else: langkah.append(("5️⃣  Integralkan Kedua Ruas",
            f"∫ {sympy_ke_html(1/ruas_kanan)} dv = ∫ {sympy_ke_html(1/x)} dx\n\n"
            f"Hasil integrasi:\n"
            f"   {sympy_ke_html(integral_kiri)} = {sympy_ke_html(integral_kanan)} + C\n\n"
            f"Substitusi kembali v = y/x"
    ))

    # Langkah 6: Solusi umum
    y_fungsi = sp.Function('y')
    pd = sp.Eq(y_fungsi(x).diff(x), ekspresi.subs(y, y_fungsi(x)))
    solusi = sp.dsolve(pd)

    solusi_html = rapikan_solusi_html(solusi)

    langkah.append(("6️⃣  Solusi Umum", solusi_html))

    return langkah


def format_teks_pecahan(teks):
    import re

    def ganti_pecahan(atas, bawah):
        atas  = re.sub(r'\*\*(\d+)', r'<sup>\1</sup>', atas)
        bawah = re.sub(r'\*\*(\d+)', r'<sup>\1</sup>', bawah)
        atas  = atas.replace("*", "")
        bawah = bawah.replace("*", "")
        return f'<span class="pecahan"><span class="pecahan-atas">{atas}</span><span class="pecahan-bawah">{bawah}</span></span>'

    # Prioritas 1: (sesuatu)**angka / (sesuatu)**angka — kurung tetap disertakan
    def ganti_p1(m):
        atas  = f"({m.group(1)}){m.group(2)}"   # (isi)**angka
        bawah = f"({m.group(3)}){m.group(4)}"   # (isi)**angka
        return ganti_pecahan(atas, bawah)

    teks = re.sub(
        r'\(([^)]+)\)(\*\*\d+)\s*/\s*\(([^)]+)\)(\*\*\d+)',
        ganti_p1, teks
    )

    # Prioritas 2: (sesuatu)/(sesuatu)
    teks = re.sub(
        r'\(([^)]+)\)\s*/\s*\(([^)]+)\)',
        lambda m: ganti_pecahan(m.group(1), m.group(2)),
        teks
    )

    # Prioritas 3: kata**angka / kata**angka
    teks = re.sub(
        r'([a-zA-Z]+\*\*\d+)\s*/\s*([a-zA-Z]+\*\*\d+)',
        lambda m: ganti_pecahan(m.group(1), m.group(2)),
        teks
    )

    # Prioritas 4: kata/kata sederhana
    teks = re.sub(
        r'(?<!\()\b([a-zA-Z]+)\b\s*/\s*\b([a-zA-Z]+)\b(?!\))',
        lambda m: ganti_pecahan(m.group(1), m.group(2)),
        teks
    )

    # Ganti sisa ** menjadi superscript
    teks = re.sub(r'\*\*(\d+)', r'<sup>\1</sup>', teks)

    # Ganti * menjadi ·
    teks = teks.replace("*", "")

    return teks

# ════════════════════════════════════════════════════════════
# BANK SOAL KUIS
# ════════════════════════════════════════════════════════════
bank_soal = [
    {"soal": "(x + y) / x",          "label": "(x + y) / x"},
    {"soal": "(y**2 - x**2)/(2*x*y)", "label": "(y² - x²) / (2xy)"},
    {"soal": "(x**2 + 2*x*y)/x**2",  "label": "(x² + 2xy) / x²"},
    {"soal": "y / x",                "label": "y / x"},
    {"soal": "(x**2+y**2)/(x*y)",    "label": "(x² + y²) / (xy)"},
    {"soal": "(x - y)/(x + y)",      "label": "(x - y) / (x + y)"},
    {"soal": "2*y/x",                "label": "2y / x"},
]

# ════════════════════════════════════════════════════════════
# INISIALISASI SESSION STATE
# ════════════════════════════════════════════════════════════
if 'skor'       not in st.session_state: st.session_state.skor       = 0
if 'total'      not in st.session_state: st.session_state.total      = 0
if 'soal_index' not in st.session_state: st.session_state.soal_index = random.randint(0, len(bank_soal)-1)
if 'sudah_jawab'not in st.session_state: st.session_state.sudah_jawab= False
if 'hasil_kuis' not in st.session_state: st.session_state.hasil_kuis = None

# ════════════════════════════════════════════════════════════
# HEADER
# ════════════════════════════════════════════════════════════
st.markdown("""
<div class="header-box">
    <h1>🧮 Aplikasi PD Homogen</h1>
    <p>Kalkulator · Langkah Penyelesaian · Kuis Latihan</p>
    <p style="margin-top:8px; font-size:0.8rem; opacity:0.6;">
        Kelompok 2 &nbsp;|&nbsp; Persamaan Differensial Homogen Derajat 0
    </p>
</div>
""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB NAVIGASI
# ════════════════════════════════════════════════════════════
tab1, tab2, tab3 = st.tabs(["🔢  Kalkulator", "📖  Langkah Penyelesaian", "✏️  Kuis Latihan"])

# ════════════════════════════════════════════════════════════
# TAB 1: KALKULATOR
# ════════════════════════════════════════════════════════════
with tab1:
    st.markdown("""
    <div class="info-box">
        ⚡ Gunakan <b>*</b> untuk perkalian (contoh: x*y) &nbsp;|&nbsp;
        Pangkat boleh pakai <b>^</b> atau <b>**</b> (contoh: x^2 atau x**2)
    </div>
    """, unsafe_allow_html=True)

    ekspresi_str = st.text_input(
        "Masukkan dy/dx =",
        placeholder="contoh: (x + y) / x",
        key="kalkulator_input"
    )

    pakai_syarat = st.checkbox("Pakai syarat awal?")

    if pakai_syarat:
        st.markdown("""
        <div class="info-box">Format: y(x_awal) = y_awal</div>
        """, unsafe_allow_html=True)
        kol1, kol2 = st.columns(2)
        with kol1:
            x_awal = st.number_input("x awal", value=1.0, key="x_awal")
        with kol2:
            y_awal = st.number_input("y awal", value=0.0, key="y_awal")

    if st.button("✨ Selesaikan!", type="primary", key="btn_kalkulator"):
        if not ekspresi_str.strip():
            st.markdown("""
            <div class="hasil-peringatan">⚠️ Masukkan persamaan differensial terlebih dahulu.</div>
            """, unsafe_allow_html=True)
        else:
            try:
                # Bersihkan input: ^ → **
                ekspresi_bersih = bersihkan_input(ekspresi_str)
                fungsi_pd = sp.sympify(ekspresi_bersih, locals={"x": x, "y": y})

                with st.spinner("Mengecek homogenitas..."):
                    homogen = cek_homogen(fungsi_pd)

                if homogen:
                    pd, y_fungsi = selesaikan_pd(fungsi_pd)

                    if pakai_syarat:
                        solusi_umum = sp.dsolve(pd)
                        if isinstance(solusi_umum, list):
                            solusi_umum = solusi_umum[0]
                        nilai_c = sp.solve(
                            solusi_umum.subs(x, x_awal).subs(y_fungsi(x_awal), y_awal),
                            C1
                        )
                        if nilai_c:
                            angka_c = nilai_c[0]
                            solusi_html = rapikan_solusi_html(solusi_umum)
                            # Ambil bagian kanan dari "C = ..."
                            ruas_html = solusi_html.split("C = ", 1)[1] if "C = " in solusi_html else solusi_html
                            st.markdown(f"""
                            <div class="solusi-box">
                                ✅ PD HOMOGEN DERAJAT 0<br><br>
                                <b>Solusi Khusus:</b><br>
                                {rapikan_angka(angka_c)} = {ruas_html}
                                <br><br>
                                <span style="font-size:0.85rem; opacity:0.7;">
                                (dengan syarat awal y({x_awal}) = {y_awal})
                                </span>
                            </div>""", unsafe_allow_html=True)
                        else:
                            st.markdown("""
                            <div class="hasil-peringatan">
                            ⚠️ Tidak dapat menentukan solusi khusus dengan syarat awal tersebut.
                            </div>""", unsafe_allow_html=True)
                    else:
                        with st.spinner("Menyelesaikan PD..."):
                            solusi = sp.dsolve(pd)
                        solusi_html = rapikan_solusi_html(solusi)
                        st.markdown(f"""
                        <div class="solusi-box">
                            ✅ PD HOMOGEN DERAJAT 0<br><br>
                            <b>Solusi Umum:</b><br>
                            {solusi_html}
                        </div>""", unsafe_allow_html=True)
                else:
                    st.markdown("""
                    <div class="hasil-gagal">
❌ PD TIDAK HOMOGEN DERAJAT 0
Program ini hanya menyelesaikan PD homogen derajat 0.
                    </div>""", unsafe_allow_html=True)

            except Exception as err:
                st.markdown(f"""
                <div class="hasil-gagal">
❌ Error: {err}
Periksa kembali format penulisan PD-nya.
                </div>""", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB 2: LANGKAH PENYELESAIAN
# ════════════════════════════════════════════════════════════
with tab2:
    st.markdown("""
    <div class="info-box">
        Masukkan PD homogen, program akan menampilkan setiap langkah penyelesaiannya secara detail.<br>
        Pangkat boleh pakai <b>^</b> atau <b>**</b>
    </div>
    """, unsafe_allow_html=True)

    ekspresi_langkah = st.text_input(
        "Masukkan dy/dx =",
        placeholder="contoh: (x + y) / x",
        key="langkah_input"
    )

    if st.button("📖 Tampilkan Langkah!", key="btn_langkah"):
        if not ekspresi_langkah.strip():
            st.markdown("""
            <div class="hasil-peringatan">⚠️ Masukkan persamaan differensial terlebih dahulu.</div>
            """, unsafe_allow_html=True)
        else:                                               # ← else ini masuk ke dalam if st.button
            try:
                ekspresi_langkah_bersih = bersihkan_input(ekspresi_langkah)
                fungsi_pd = sp.sympify(ekspresi_langkah_bersih, locals={"x": x, "y": y})

                if not cek_homogen(fungsi_pd):
                    st.markdown("""
                    <div class="hasil-gagal">❌ PD TIDAK HOMOGEN DERAJAT 0.</div>
                    """, unsafe_allow_html=True)
                else:
                    with st.spinner("Menyusun langkah penyelesaian..."):
                        langkah_list = buat_langkah(ekspresi_langkah_bersih, fungsi_pd)

                    for i, (judul_l, isi_l) in enumerate(langkah_list):
                        st.markdown(f"""
                        <div class="langkah-judul">{judul_l}</div>
                        """, unsafe_allow_html=True)
                    
                        if i == 0:
                            # Proses seluruh teks termasuk dy/dx sebagai pecahan
                            isi_html = format_teks_pecahan(isi_l)
                            st.markdown(isi_html, unsafe_allow_html=True)
                    
                        elif i == 1:
                            ekspresi_obj = fungsi_pd
                        
                            # Ganti x dan y di string dengan cara yang aman
                            # pakai regex agar hanya ganti x dan y yang berdiri sendiri
                            import re
                            ekspresi_mentah_str = re.sub(r'\bx\b', '(t*x)', ekspresi_langkah_bersih)
                            ekspresi_mentah_str = re.sub(r'\by\b', '(t*y)', ekspresi_mentah_str)
                        
                            # Hasil SymPy
                            ekspresi_diganti   = ekspresi_obj.subs(x, t*x).subs(y, t*y)
                            ekspresi_sederhana = sp.simplify(ekspresi_diganti)
                            hasil_bagi         = sp.simplify(ekspresi_diganti / ekspresi_obj)
                        
                            html_asli          = sympy_ke_html(ekspresi_obj)
                            ekspresi_mentah = ekspresi_obj.subs(x, t*x).subs(y, t*y)
                            html_mentah = sympy_ke_html(ekspresi_mentah)
                            html_sederhana     = sympy_ke_html(ekspresi_sederhana)
                            html_hasil         = sympy_ke_html(hasil_bagi)
                        
                            # Tampilkan dengan urutan yang benar
                            st.markdown("Ganti x → tx &nbsp; dan &nbsp; y → ty :", unsafe_allow_html=True)
                            st.markdown(f"**f(x, y)** &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp;{html_asli}", unsafe_allow_html=True)
                            st.markdown(f"**f(tx, ty)** = &nbsp;{html_mentah}", unsafe_allow_html=True)
                            st.markdown(f"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp;{html_sederhana} &nbsp;*(setelah disederhanakan)*", unsafe_allow_html=True)
                            st.markdown(f"""
                            <span class="pecahan">
                                <span class="pecahan-atas">f(tx,&nbsp;ty)</span>
                                <span class="pecahan-bawah">f(x,&nbsp;y)</span>
                            </span>
                            &nbsp;= &nbsp;{html_hasil}
                            """, unsafe_allow_html=True)
                            st.success("✓ Variabel t hilang → PD Homogen Derajat 0")                                            
                        else:
                            isi_l = isi_l.replace("*", "")
                            isi_html = format_teks_pecahan(isi_l)
                            st.markdown(isi_html, unsafe_allow_html=True)

            except Exception as err:
                st.markdown(f"""
                <div class="hasil-gagal">❌ Error: {err}</div>
                """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB 3: KUIS LATIHAN
# ════════════════════════════════════════════════════════════
with tab3:
    st.markdown(f"""
    <div class="skor-box">
        <div class="skor-angka">{st.session_state.skor}/{st.session_state.total}</div>
        <div class="skor-label">Skor Kuis</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-box">
        Tentukan solusi umum dari PD berikut dalam bentuk <b>C = ...</b><br>
        Pangkat boleh pakai <b>^</b> atau <b>**</b>, perkalian pakai <b>*</b>
    </div>
    """, unsafe_allow_html=True)

    soal_skrg = bank_soal[st.session_state.soal_index]
    st.markdown(f"""
    <div class="soal-box">dy/dx = {soal_skrg['label']}</div>
    """, unsafe_allow_html=True)

    jawaban_user = st.text_input(
        "C = ",
        placeholder="tulis jawaban di sini...",
        key="jawaban_kuis",
        disabled=st.session_state.sudah_jawab
    )

    kol1, kol2, kol3 = st.columns([1, 1, 1])

    with kol1:
        if st.button("✅ Jawab!", type="primary", disabled=st.session_state.sudah_jawab):
            if not jawaban_user.strip():
                st.warning("Tulis jawaban dulu!")
            else:
                st.session_state.total += 1
                st.session_state.sudah_jawab = True
                try:
                    fungsi_pd = sp.sympify(soal_skrg['soal'], locals={"x": x, "y": y})
                    pd, y_fungsi = selesaikan_pd(fungsi_pd)
                    solusi = sp.dsolve(pd)
                    jawaban_benar_str = rapikan_solusi_teks(solusi)
                    ruas_benar = jawaban_benar_str.split("C = ")[1] if "C = " in jawaban_benar_str else jawaban_benar_str

                    try:
                        # Bersihkan jawaban user sebelum dicek
                        jawaban_bersih = bersihkan_input(jawaban_user)
                        eksp_user  = sp.sympify(jawaban_bersih, locals={"x": x, "y": y})
                        eksp_benar = sp.sympify(ruas_benar.replace("^", "**"), locals={"x": x, "y": y})
                        selisih = sp.simplify(eksp_user - eksp_benar)
                        benar = selisih == 0 or sp.simplify(eksp_user / eksp_benar).is_number
                    except:
                        benar = False

                    if benar:
                        st.session_state.skor += 1
                        st.session_state.hasil_kuis = ("benar", ruas_benar)
                    else:
                        st.session_state.hasil_kuis = ("salah", ruas_benar)

                except Exception as err:
                    st.session_state.hasil_kuis = ("error", str(err))

                st.rerun()

    with kol2:
        if st.button("➡️ Soal Baru"):
            st.session_state.soal_index  = random.randint(0, len(bank_soal)-1)
            st.session_state.sudah_jawab = False
            st.session_state.hasil_kuis  = None
            st.rerun()

    with kol3:
        if st.button("🔄 Reset Skor", type="secondary"):
            st.session_state.skor        = 0
            st.session_state.total       = 0
            st.session_state.soal_index  = random.randint(0, len(bank_soal)-1)
            st.session_state.sudah_jawab = False
            st.session_state.hasil_kuis  = None
            st.rerun()

    if st.session_state.hasil_kuis:
        status, info = st.session_state.hasil_kuis
        if status == "benar":
            st.markdown(f"""
            <div class="hasil-sukses">
✅ BENAR! Bagus sekali!

Jawaban: C = {info}
            </div>""", unsafe_allow_html=True)
        elif status == "salah":
            st.markdown(f"""
            <div class="hasil-gagal">
❌ SALAH.

Jawabanmu : C = {jawaban_user}
Yang benar: C = {info}
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="hasil-gagal">❌ Error: {info}</div>
            """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    🧮 Aplikasi PD Homogen &nbsp;|&nbsp; Kelompok 2 &nbsp;|&nbsp;
    Dibuat dengan Python · SymPy · Streamlit
</div>
""", unsafe_allow_html=True)
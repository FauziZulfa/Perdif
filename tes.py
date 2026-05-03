import streamlit as st
import sympy as sp
import random
import re


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
/* Paksa dark mode */
html, body, [class*="css"], .stApp {
    background-color: #0e1117 !important;
    color: #fafafa !important;
}

/* Input box */
.stTextInput input {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

/* Checkbox */
.stCheckbox label {
    color: #fafafa !important;
}

/* Tab */
.stTabs [data-baseweb="tab-list"] {
    background-color: #0e1117 !important;
}

.stTabs [data-baseweb="tab"] {
    color: #fafafa !important;
}

/* Number input */
.stNumberInput input {
    background-color: #262730 !important;
    color: #fafafa !important;
}

/* Tombol */
.stButton button {
    background-color: #262730 !important;
    color: #fafafa !important;
    border: 1px solid #444 !important;
}

            /* Paksa warna teks label input selalu putih */
.stTextInput label, 
.stNumberInput label,
.stCheckbox label,
.stSelectbox label {
    color: #fafafa !important;
}

/* Placeholder teks di dalam kotak input */
.stTextInput input::placeholder {
    color: #aaaaaa !important;
}

/* Paksa warna teks checkbox */
.stCheckbox p,
.stCheckbox span,
.stCheckbox label,
[data-testid="stCheckbox"] p,
[data-testid="stCheckbox"] span,
[data-testid="stCheckbox"] label {
    color: #fafafa !important;
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
    """
    Membersihkan input pengguna agar bisa diproses oleh Sympy.
    - Mengganti ^ dengan **
    - Menghapus spasi
    - Melindungi nama fungsi agar tidak rusak
    - Menyisipkan * secara otomatis di tempat yang tepat
    """
    # Daftar fungsi yang harus dilindungi (case sensitive)
    func_names = [
        "sin", "cos", "tan", "csc", "sec", "cot",
        "arcsin", "arccos", "arctan",
        "sinh", "cosh", "tanh",
        "log", "ln", "exp", "sqrt"
    ]
    
    # Simpan placeholder untuk setiap fungsi
    placeholders = {}
    for i, fn in enumerate(func_names):
        placeholder = f"__FUNC{i}__"
        placeholders[fn] = placeholder

    # Urutkan fungsi dari yang terpanjang agar tidak tertabrak penggantian parsial
    sorted_funcs = sorted(func_names, key=len, reverse=True)
    for fn in sorted_funcs:
        # Hanya ganti jika diikuti oleh '(' (agar tidak mengganti variabel bernama sama)
        teks = re.sub(r'\b' + fn + r'(?=\()', placeholders[fn], teks)

    # Operasi pembersihan dasar
    teks = teks.replace(" ", "")          # hilangkan semua spasi
    teks = teks.replace("^", "**")        # ubah ^ menjadi ** untuk pangkat

    # Tambahkan * secara implisit pada pola-pola tertentu
    # 2x → 2*x
    teks = re.sub(r'(\d)([a-zA-Z])', r'\1*\2', teks)
    # )( → )*(  (misal: (x+1)(x+2))
    teks = re.sub(r'\)(\()', r')*\1', teks)
    # )angka → )*angka
    teks = re.sub(r'\)(\d)', r')*\1', teks)
    # )huruf → )*huruf  (hati-hati dengan fungsi, tapi fungsi sudah dilindungi placeholder)
    teks = re.sub(r'\)([a-zA-Z])', r')*\1', teks)

    # Kembalikan placeholder ke nama fungsi asli
    for fn, ph in placeholders.items():
        teks = teks.replace(ph, fn)

    return teks


def cek_homogen(ekspresi):
    """Mengecek apakah PD homogen derajat 0 atau tidak."""
    # Pastikan ekspresi mengandung x dan y
    simbol_yang_dikenal = {x, y}
    simbol_dalam_ekspresi = ekspresi.free_symbols
    
    # Cek simbol asing (selain x, y, t)
    simbol_tak_dikenal = simbol_dalam_ekspresi - simbol_yang_dikenal - {t}
    if simbol_tak_dikenal:
        raise ValueError(f"Ekspresi mengandung simbol tak dikenal: {simbol_tak_dikenal}\n"
                        f"Gunakan hanya variabel x dan y.")
    
    # Cek apakah ekspresi dependen pada x dan y
    if len(simbol_dalam_ekspresi.intersection({x, y})) == 0:
        raise ValueError("Ekspresi tidak mengandung variabel x dan/atau y. "
                        "PD homogen harus fungsi dari x dan y.")
    
    # Uji homogenitas
    try:
        ekspresi_diganti = ekspresi.subs(x, t*x).subs(y, t*y)
        hasil = sp.simplify(ekspresi_diganti / ekspresi)
        return t not in hasil.free_symbols
    except:
        return False

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

def sympy_ke_html(eksp, sederhanakan_dulu=True):
    """Ubah ekspresi Sympy menjadi HTML dengan pecahan dan superscript."""
    import re

    if sederhanakan_dulu:
        eksp = sp.together(eksp)

    pembilang = sp.numer(eksp)
    penyebut  = sp.denom(eksp)

    def format_bagian(bagian):
        teks = str(bagian)\
            .replace("log(", "ln(")\
            .replace("atan(", "arctan(")
        teks = re.sub(r'(\w+)\*\*(\d+)', r'\1<sup>\2</sup>', teks)
        teks = teks.replace("*", "")
        return teks

    if penyebut != 1:
        return f'<span class="pecahan"><span class="pecahan-atas">{format_bagian(pembilang)}</span><span class="pecahan-bawah">{format_bagian(penyebut)}</span></span>'
    else:
        return format_bagian(pembilang)

def rapikan_solusi_html(solusi, integrand_v=None, integral_kanan=None):
    """
    Solusi ke HTML. Jika solusi mengandung Integral dan integrand_v disediakan,
    tampilkan bentuk: ∫ (integrand_v) dv = integral_kanan + C.
    """
    C = sp.Symbol('C')

    def proses(s):
        persamaan = s.subs(C1, C)
        c_solusi = sp.solve(persamaan, C)
        if c_solusi:
            if isinstance(c_solusi[0], sp.Eq):
                eksp = sederhanakan(c_solusi[0].rhs)
            else:
                eksp = sederhanakan(c_solusi[0])
        else:
            eksp = sederhanakan(s.rhs.subs(C1, C))

        if eksp.has(sp.Integral) and integrand_v is not None and integral_kanan is not None:
            return (f"&int; {sympy_ke_html(integrand_v)} dv = "
                    f"{sympy_ke_html(integral_kanan)} + C<br>"
                    f"(v = y/x)")
        else:
            return f"C = {sympy_ke_html(eksp)}"

    if isinstance(solusi, list):
        hasil = list(dict.fromkeys([proses(s) for s in solusi]))
        return "<br>".join(hasil)
    return proses(solusi)


def rapikan_solusi_teks(solusi, integrand_v=None, integral_kanan=None):
    """Solusi teks biasa."""
    C = sp.Symbol('C')

    def proses(s):
        persamaan = s.subs(C1, C)
        c_solusi = sp.solve(persamaan, C)
        if c_solusi:
            if isinstance(c_solusi[0], sp.Eq):
                eksp = sederhanakan(c_solusi[0].rhs)
            else:
                eksp = sederhanakan(c_solusi[0])
        else:
            eksp = sederhanakan(s.rhs.subs(C1, C))

        if eksp.has(sp.Integral) and integrand_v is not None and integral_kanan is not None:
            return (f"∫ {str(integrand_v)} dv = "
                    f"{str(integral_kanan)} + C  (v = y/x)")
        else:
            rapi = str(eksp).replace("log(", "ln(").replace("atan(", "arctan(")
            return f"C = {rapi}"

    if isinstance(solusi, list):
        hasil = list(dict.fromkeys([proses(s) for s in solusi]))
        return "\n".join(hasil)
    return proses(solusi)

def rapikan_angka(angka):
    """Membulatkan angka maksimal 3 desimal dan menghapus nol tidak perlu."""
    return f"{float(angka):.3f}".rstrip('0').rstrip('.')

def buat_langkah(ekspresi_str, ekspresi):
    """Susun langkah-langkah penyelesaian."""
    langkah = []

    # Langkah 1: Tulis bentuk PD
    langkah.append(("1️⃣  Bentuk PD",
        f"dy/dx = {ekspresi_str}"))

    # Langkah 2: Uji homogenitas
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
    langkah.append(("3️⃣  Misalkan y = vx",
        "  Misal:   y = vx  sehingga  v = y/x  ...(1)\n\n"
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
            f"Substitusi (1) dan (2):\n\n"
            f"v + x dv/dx = {sympy_ke_html(ekspresi_v)}\n\n"
            f"x dv/dx = 0\n\n"
            f"dv/dx = 0"
        ))
    else:
        langkah.append(("4️⃣  Bentuk Setelah Substitusi",
            f"dy/dx = {sympy_ke_html(ekspresi)}\n\n"
            f"Substitusi (1) dan (2):\n\n"
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
            "Hasil Integrasi:\n"
            "v = C\n\n"
            "Substitusi kembali v = y/x → y = Cx"
        ))
    else:
        langkah.append(("5️⃣  Integralkan Kedua Ruas",
            f"∫ {sympy_ke_html(1/ruas_kanan)} dv = ∫ {sympy_ke_html(1/x)} dx\n\n"
            f"Hasil Integrasi:\n"
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
    """Mengubah teks matematika (string) menjadi HTML dengan pecahan dan superscript."""
    import re

    def format_isi(bagian):
        bagian = re.sub(r'\*\*(\d+)', r'<sup>\1</sup>', bagian)
        bagian = bagian.replace("*", "")
        return bagian

    def ganti_pecahan(atas, bawah):
        return f'<span class="pecahan"><span class="pecahan-atas">{format_isi(atas)}</span><span class="pecahan-bawah">{format_isi(bawah)}</span></span>'

    def ganti_p1(m):
        atas  = f"({m.group(1)}){m.group(2)}"
        bawah = f"({m.group(3)}){m.group(4)}"
        return ganti_pecahan(atas, bawah)

    teks = re.sub(r'\(([^)]+)\)(\*\*\d+)\s*/\s*\(([^)]+)\)(\*\*\d+)', ganti_p1, teks)
    teks = re.sub(r'\(([^)]+)\)\s*/\s*\(([^)]+)\)',
                  lambda m: ganti_pecahan(m.group(1), m.group(2)), teks)
    teks = re.sub(r'\(([^)]+)\)\s*/\s*([a-zA-Z]+\*\*\d+)',
                  lambda m: ganti_pecahan(m.group(1), m.group(2)), teks)
    teks = re.sub(r'([a-zA-Z0-9]+\*\*\d+)\s*/\s*([a-zA-Z0-9]+\*\*\d+)',
                  lambda m: ganti_pecahan(m.group(1), m.group(2)), teks)
    teks = re.sub(r'(\d+\*[a-zA-Z]+)\s*/\s*([a-zA-Z]+)',
                  lambda m: ganti_pecahan(m.group(1), m.group(2)), teks)
    teks = re.sub(
        r'\b([a-zA-Z]+)\*\*(\d+)\s*/\s*\b([a-zA-Z]+)\b',
        lambda m: f'<span class="pecahan"><span class="pecahan-atas">{m.group(1)}<sup>{m.group(2)}</sup></span><span class="pecahan-bawah">{m.group(3)}</span></span>',
        teks
    )
    teks = re.sub(
        r'\b([a-zA-Z]+)\b\s*/\s*([a-zA-Z]+)\*\*(\d+)',
        lambda m: f'<span class="pecahan"><span class="pecahan-atas">{m.group(1)}</span><span class="pecahan-bawah">{m.group(2)}<sup>{m.group(3)}</sup></span></span>',
        teks
    )
    teks = re.sub(r'(?<!\()\b([a-zA-Z]+)\b\s*/\s*\b([a-zA-Z]+)\b(?!\))',
                  lambda m: ganti_pecahan(m.group(1), m.group(2)), teks)
    teks = re.sub(r'\*\*(\d+)', r'<sup>\1</sup>', teks)
    teks = teks.replace("*", "")
    return teks


def validasi_ekspresi(ekspresi_str, ekspresi):
    """Validasi hanya x dan y yang menjadi variabel."""
    simbol_tak_dikenal = ekspresi.free_symbols - {x, y}
    if simbol_tak_dikenal:
        raise ValueError(f"❌ Simbol '{simbol_tak_dikenal}' tidak dikenal!\n"
                        f"Hanya gunakan variabel x dan y, serta fungsi matematika standar.\n"
                        f"Contoh: sin(x), cos(y), log(x), exp(x), dll.")
    if len(ekspresi.free_symbols.intersection({x, y})) == 0:
        raise ValueError("❌ Ekspresi harus mengandung variabel x dan/atau y!\n"
                        f"Contoh: x+y, (x**2 + y**2)/(x*y), dll.")
    return True

# ════════════════════════════════════════════════════════════
# BANK SOAL KUIS
# ════════════════════════════════════════════════════════════
bank_soal = [
    {"soal": "(x + y) / x",              "label": "(x + y) / (x)"},
    {"soal": "(y**2 - x**2)/(2*x*y)",    "label": "(y**2 - x**2) / (2*x*y)"},
    {"soal": "(x**2 + 2*x*y)/x**2",      "label": "(x**2 + 2*x*y) / (x**2)"},
    {"soal": "y / x",                    "label": "y / x"},
    {"soal": "(x**2+y**2)/(x*y)",        "label": "(x**2 + y**2) / (x*y)"},
    {"soal": "(x - y)/(x + y)",          "label": "(x - y) / (x + y)"},
    {"soal": "2*y/x",                    "label": "2*y / x"},
    {"soal": "(x**2 - y**2)/(x*y)",      "label": "(x**2 - y**2) / (x*y)"},
    {"soal": "(x**2 + x*y)/(x**2)",      "label": "(x**2 + x*y) / x**2"},
]

JUMLAH_SOAL = len(bank_soal)

# ════════════════════════════════════════════════════════════
# INISIALISASI SESSION STATE
# ════════════════════════════════════════════════════════════
if 'skor'        not in st.session_state: st.session_state.skor        = 0
if 'soal_index'  not in st.session_state: st.session_state.soal_index  = 0
if 'sudah_jawab' not in st.session_state: st.session_state.sudah_jawab = False
if 'hasil_kuis'  not in st.session_state: st.session_state.hasil_kuis  = None
if 'jawaban_per_soal' not in st.session_state: st.session_state.jawaban_per_soal = {}
if 'tampil_balon' not in st.session_state: st.session_state.tampil_balon = False

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
        ⚡ Gunakan <b>^</b> untuk pangkat (contoh: x^2)<br>
        ⚡ Gunakan <b>*</b> untuk perkalian (contoh: x*y)
    </div>
    """, unsafe_allow_html=True)

    ekspresi_str = st.text_input(
        "Masukkan dy/dx =",
        placeholder="contoh: (x + y) / (x - y)",
        key="kalkulator_input"
    )
    
    st.markdown("""
    <div style="font-size:0.85rem; background:#fef3c7; padding:8px 12px; border-radius:6px; border-left:4px solid #f59e0b; color:#78350f;margin-bottom:15px;">
    ⚠️ Perhatikan tanda kurung! Misal: (x + y) / (x - y), bukan x + y / x - y
    </div>
    """, unsafe_allow_html=True)

    pakai_syarat = st.checkbox("Pakai syarat awal?")

    if pakai_syarat:
        st.markdown("""
        <div class="info-box">Format: y(x) = a</div>
        """, unsafe_allow_html=True)
        kol1, kol2 = st.columns(2)
        with kol1:
            x_awal = st.number_input("Masukkan nilai x : ", value=0.0, key="x_awal", step=1.0)
        with kol2:
            y_awal = st.number_input("Masukkan nilai a :", value=0.0, key="y_awal", step=1.0)

    if st.button("✨ Selesaikan!", type="primary", key="btn_kalkulator"):
        if not ekspresi_str.strip():
            st.markdown("""
            <div class="hasil-peringatan">⚠️ Masukkan persamaan differensial terlebih dahulu.</div>
            """, unsafe_allow_html=True)
        else:
            try:
                ekspresi_bersih = bersihkan_input(ekspresi_str)
                fungsi_pd = sp.sympify(ekspresi_bersih, locals={"x": x, "y": y})
                
                validasi_ekspresi(ekspresi_str, fungsi_pd)

                with st.spinner("Mengecek homogenitas..."):
                    homogen = cek_homogen(fungsi_pd)

                 if homogen:
                    
                    # Siapkan integrand dan integral untuk fallback tampilan
                    ekspresi_v = sp.simplify(fungsi_pd.subs(y, v*x))
                    ruas_kanan = sp.simplify(ekspresi_v - v)
                    if not sp.simplify(ruas_kanan).is_zero:
                        integrand_v = 1 / ruas_kanan
                        integral_kanan = sp.integrate(1/x, x)
                    else:
                        integrand_v = None
                        integral_kanan = None
                
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
                            if isinstance(angka_c, sp.Eq):
                                angka_c = angka_c.rhs
                            solusi_html = rapikan_solusi_html(solusi_umum, integrand_v, integral_kanan)
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
                            st.warning("⚠️ Tidak dapat menentukan solusi khusus.")
                    else:
                        with st.spinner("Menyelesaikan PD..."):
                            solusi = sp.dsolve(pd)
                        solusi_html = rapikan_solusi_html(solusi, integrand_v, integral_kanan)
                        st.markdown(f"""
                        <div class="solusi-box">
                            ✅ PD HOMOGEN DERAJAT 0<br><br>
                            <b>Solusi Umum:</b><br>
                            {solusi_html}
                        </div>""", unsafe_allow_html=True)

            except ValueError as ve:
                st.markdown(f'<div class="hasil-gagal">{ve}</div>', unsafe_allow_html=True)
            except Exception as err:
                st.markdown(f'<div class="hasil-gagal">❌ Error: {err}</div>', unsafe_allow_html=True)

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
            ⚡ Gunakan <b>^</b> untuk pangkat (contoh: x^2)<br>
            ⚡ Gunakan <b>*</b> untuk perkalian (contoh: x*y)
        </div>
        """, unsafe_allow_html=True)

    ekspresi_langkah = st.text_input(
        "Masukkan dy/dx =",
        placeholder="contoh: (x + y) / (x - y)",
        key="langkah_input"
    )

    st.markdown("""
        <div style="font-size:0.85rem; background:#fef3c7; padding:8px 12px; border-radius:6px; border-left:4px solid #f59e0b; color:#78350f;margin-bottom:15px;">
        ⚠️ Perhatikan tanda kurung! Misal: (x + y) / (x - y), bukan x + y / x - y
        </div>
        """, unsafe_allow_html=True)

    if st.button("📖 Tampilkan Langkah!", key="btn_langkah"):
        if not ekspresi_langkah.strip():
            st.markdown("""
            <div class="hasil-peringatan">⚠️ Masukkan persamaan differensial terlebih dahulu.</div>
            """, unsafe_allow_html=True)
        else:
            try:
                ekspresi_bersih = bersihkan_input(ekspresi_langkah)
                fungsi_pd = sp.sympify(ekspresi_bersih, locals={"x": x, "y": y})

                if not cek_homogen(fungsi_pd):
                    st.markdown('<div class="hasil-gagal">❌ PD TIDAK HOMOGEN DERAJAT 0.</div>', unsafe_allow_html=True)
                else:
                    with st.spinner("Menyusun langkah penyelesaian..."):
                        langkah_list = buat_langkah(ekspresi_bersih, fungsi_pd)

                    for i, (judul_l, isi_l) in enumerate(langkah_list):
                        st.markdown(f'<div class="langkah-judul">{judul_l}</div>', unsafe_allow_html=True)
                        if i == 0:
                            st.markdown(format_teks_pecahan(isi_l), unsafe_allow_html=True)
                        elif i == 1:
                            ekspresi_obj = fungsi_pd
                            ekspresi_mentah = ekspresi_obj.subs(x, t*x).subs(y, t*y)
                            if t not in ekspresi_mentah.free_symbols:
                                tx = sp.Symbol('tx')
                                ty = sp.Symbol('ty')
                                ekspresi_mentah = ekspresi_obj.subs(x, tx).subs(y, ty)
                            html_mentah = sympy_ke_html(ekspresi_mentah, sederhanakan_dulu=False)
                            ekspresi_sederhana = sp.simplify(ekspresi_obj.subs(x, t*x).subs(y, t*y))
                            hasil_bagi = sp.simplify(ekspresi_obj.subs(x, t*x).subs(y, t*y) / ekspresi_obj)
                            html_asli = sympy_ke_html(ekspresi_obj)
                            html_sederhana = sympy_ke_html(ekspresi_sederhana)
                            html_hasil = sympy_ke_html(hasil_bagi)
                            st.markdown("Ganti x → tx &nbsp; dan &nbsp; y → ty :", unsafe_allow_html=True)
                            st.markdown(f"**f(x, y)** = {html_asli}", unsafe_allow_html=True)
                            st.markdown(f"**f(tx, ty)** = {html_mentah} &nbsp;= {html_sederhana} *(setelah disederhanakan)*", unsafe_allow_html=True)
                            st.markdown(f"<span class='pecahan'><span class='pecahan-atas'>f(tx, ty)</span><span class='pecahan-bawah'>f(x, y)</span></span> = {html_hasil}", unsafe_allow_html=True)
                            st.success("✓ Variabel t hilang → PD Homogen Derajat 0")
                        else:
                            isi_l = isi_l.replace("*", "")
                            st.markdown(format_teks_pecahan(isi_l), unsafe_allow_html=True)

            except Exception as err:
                st.markdown(f"""
                <div class="hasil-gagal">❌ Error: {err}</div>
                """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# TAB 3: KUIS LATIHAN
# ════════════════════════════════════════════════════════════
with tab3:
    nomor     = st.session_state.soal_index
    soal_skrg = bank_soal[nomor]

    st.markdown(f"""
    <div class="skor-box">
        <div class="skor-angka">{st.session_state.skor}/{JUMLAH_SOAL}</div>
        <div class="skor-label">Skor Kuis</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f"""
    <div class="info-box">
        Soal <b>{nomor + 1}</b> dari <b>{JUMLAH_SOAL}</b> &nbsp;|&nbsp;
        Jawaban dalam bentuk <b>C = ...</b> &nbsp;|&nbsp;
        Gunakan <b>^</b> untuk pangkat
    </div>
    """, unsafe_allow_html=True)

    html_soal = format_teks_pecahan(soal_skrg['label'])
    st.markdown(f"""
    <div class="soal-box">
        Soal {nomor + 1}: &nbsp;
        <span class="pecahan">
            <span class="pecahan-atas">dy</span>
            <span class="pecahan-bawah">dx</span>
        </span>
        &nbsp;= &nbsp;{html_soal}
    </div>
    """, unsafe_allow_html=True)

    sudah_dijawab_sebelumnya = nomor in st.session_state.jawaban_per_soal

    jawaban_user = st.text_input(
        "C = ",
        placeholder="tulis jawaban di sini...",
        key=f"jawaban_kuis_{nomor}",
        disabled=sudah_dijawab_sebelumnya
    )

    kol1, kol2, kol3, kol4 = st.columns([1, 1, 1, 1])

    with kol1:
        if st.button("⬅️ Sebelumnya", disabled=nomor == 0):
            st.session_state.soal_index  -= 1
            st.session_state.hasil_kuis  = st.session_state.jawaban_per_soal.get(nomor - 1)
            st.rerun()

    with kol2:
        if st.button("➡️ Selanjutnya", disabled=nomor == JUMLAH_SOAL - 1):
            st.session_state.soal_index  += 1
            st.session_state.hasil_kuis  = st.session_state.jawaban_per_soal.get(nomor + 1)
            st.rerun()

    with kol3:
        if st.button("✅ Jawab!", type="primary", disabled=sudah_dijawab_sebelumnya):
            if not jawaban_user.strip():
                st.warning("Tulis jawaban dulu!")
            else:
                try:
                    fungsi_pd = sp.sympify(soal_skrg['soal'], locals={"x": x, "y": y})
                    pd_obj, y_fungsi = selesaikan_pd(fungsi_pd)
                    solusi = sp.dsolve(pd_obj)
                    jawaban_benar_str = rapikan_solusi_teks(solusi)
                    ruas_benar = jawaban_benar_str.split("C = ")[1] if "C = " in jawaban_benar_str else jawaban_benar_str

                    try:
                        jawaban_bersih = bersihkan_input(jawaban_user)
                        eksp_user  = sp.sympify(jawaban_bersih, locals={"x": x, "y": y})
                        eksp_benar = sp.sympify(ruas_benar.replace("^", "**"), locals={"x": x, "y": y})
                    
                        # Cek selisih
                        selisih = sp.simplify(eksp_user - eksp_benar)
                        cek1 = selisih == 0
                    
                        # Cek rasio (hanya beda konstanta pengali)
                        try:
                            rasio = sp.simplify(eksp_user / eksp_benar)
                            cek2 = rasio.is_number and rasio != 0
                        except:
                            cek2 = False
                    
                        # Cek setelah normalisasi koefisien
                        try:
                            koef_user  = eksp_user  / sp.gcd(tuple(sp.Poly(eksp_user,  x, y).coeffs()))
                            koef_benar = eksp_benar / sp.gcd(tuple(sp.Poly(eksp_benar, x, y).coeffs()))
                            cek3 = sp.simplify(koef_user - koef_benar) == 0
                        except:
                            cek3 = False
                    
                        benar = cek1 or cek2 or cek3
                    
                    except:
                        benar = False

                    if benar:
                        st.session_state.skor += 1
                        hasil = ("benar", ruas_benar)
                        st.session_state.tampil_balon = True
                    else:
                        hasil = ("salah", ruas_benar)

                    st.session_state.jawaban_per_soal[nomor] = hasil
                    st.session_state.hasil_kuis = hasil

                except Exception as err:
                    st.session_state.hasil_kuis = ("error", str(err))

                st.rerun()

    with kol4:
        if st.button("🔄 Reset", type="secondary"):
            st.session_state.skor             = 0
            st.session_state.soal_index       = 0
            st.session_state.sudah_jawab      = False
            st.session_state.hasil_kuis       = None
            st.session_state.jawaban_per_soal = {}
            st.rerun()

    # Tampilkan hasil
    hasil_tampil = st.session_state.jawaban_per_soal.get(nomor) or st.session_state.hasil_kuis
    
    if hasil_tampil:
        status, info = hasil_tampil
        if status == "benar":
            html_info = format_teks_pecahan(info)
            st.markdown(f"""
            <div class="hasil-sukses">
                ✅ BENAR! Bagus sekali!<br><br>
                Jawaban: C = {html_info}
            </div>""", unsafe_allow_html=True)
        elif status == "salah":
            html_info = format_teks_pecahan(info)
            st.markdown(f"""
            <div class="hasil-gagal">
                ❌ SALAH.<br><br>
                Yang benar: C = {html_info}
            </div>""", unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="hasil-gagal">❌ Error: {info}</div>', unsafe_allow_html=True)

    # Ringkasan akhir kuis
    if len(st.session_state.jawaban_per_soal) == JUMLAH_SOAL:
        benar_list = []
        salah_list = []
        for nomor_soal, (status_soal, _) in st.session_state.jawaban_per_soal.items():
            if status_soal == "benar":
                benar_list.append(nomor_soal + 1)
            else:
                salah_list.append(nomor_soal + 1)

        benar_str = ", ".join([f" {n}" for n in sorted(benar_list)]) or "-"
        salah_str = ", ".join([f" {n}" for n in sorted(salah_list)]) or "-"

        warna = "#16a34a" if st.session_state.skor >= JUMLAH_SOAL // 2 else "#dc2626"

        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, #f0fdf4, #dbeafe);
            border: 2px solid {warna};
            border-radius: 12px;
            padding: 24px;
            margin-top: 20px;
            text-align: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 8px;">🎉</div>
            <div style="font-family: 'Playfair Display', serif; font-size: 1.5rem; font-weight: bold; color: {warna};">
                Kuis Selesai!
            </div>
            <div style="font-size: 2.5rem; font-weight: bold; color: {warna}; margin: 12px 0;">
                {st.session_state.skor} / {JUMLAH_SOAL}
            </div>
            <div style="font-size: 0.9rem; color: #374151; margin-top: 12px; text-align: left; padding: 0 16px;">
                ✅ <b>Benar:</b> {benar_str}<br><br>
                ❌ <b>Salah:</b> {salah_str}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    if st.session_state.tampil_balon:
        st.balloons()
        st.session_state.tampil_balon = False

# ════════════════════════════════════════════════════════════
# FOOTER
# ════════════════════════════════════════════════════════════
st.markdown("""
<div class="footer">
    🧮 Aplikasi PD Homogen &nbsp;|&nbsp; Kelompok 2
</div>
""", unsafe_allow_html=True)
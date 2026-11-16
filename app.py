import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from io import StringIO

st.set_page_config(
    page_title="Audit SI E-Commerce | COBIT 5",
    page_icon="🛒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =========================
# DATA AUDIT DARI TUGAS 1
# =========================
PRINCIPLES = {
    "Prinsip 1 — Meeting Stakeholder Needs": [
        ("1.1", "Apakah tujuan layanan sistem informasi telah ditetapkan dan dikaitkan dengan tujuan bisnis perusahaan?"),
        ("1.2", "Apakah kebutuhan pengguna, penjual, mitra, dan unit internal dikumpulkan serta ditinjau secara berkala?"),
        ("1.3", "Apakah keluhan pengguna dan insiden layanan dicatat, diklasifikasikan, dan ditindaklanjuti?"),
        ("1.4", "Apakah risiko yang dapat memengaruhi pengguna, transaksi, dan reputasi perusahaan dinilai secara berkala?"),
        ("1.5", "Apakah indikator kinerja layanan, seperti ketersediaan sistem dan penyelesaian keluhan, dipantau?"),
    ],
    "Prinsip 2 — Covering the Enterprise End-to-End": [
        ("2.1", "Apakah tanggung jawab pengelolaan sistem informasi ditetapkan untuk unit bisnis dan unit TI yang terkait?"),
        ("2.2", "Apakah proses pesanan, pembayaran, pengiriman, dan layanan pelanggan memiliki alur kerja serta tanggung jawab yang jelas?"),
        ("2.3", "Apakah risiko dari pihak ketiga atau mitra layanan yang terhubung dengan sistem diidentifikasi dan dikelola?"),
        ("2.4", "Apakah perubahan pada sistem dikomunikasikan kepada unit yang terdampak sebelum diterapkan?"),
        ("2.5", "Apakah kebijakan keamanan dan penggunaan data berlaku bagi personel serta pihak terkait sesuai kewenangannya?"),
    ],
    "Prinsip 3 — Applying a Single Integrated Framework": [
        ("3.1", "Apakah terdapat kebijakan atau standar tertulis untuk pengembangan, pengoperasian, dan pemeliharaan sistem?"),
        ("3.2", "Apakah kebijakan keamanan informasi, privasi, dan pengelolaan data diselaraskan dengan kewajiban yang berlaku?"),
        ("3.3", "Apakah proses manajemen risiko TI terhubung dengan proses manajemen risiko perusahaan?"),
        ("3.4", "Apakah perubahan sistem mengikuti prosedur persetujuan, pengujian, dokumentasi, dan rencana pemulihan bila gagal?"),
        ("3.5", "Apakah standar dan prosedur ditinjau serta diperbarui saat teknologi, ancaman, atau kebutuhan bisnis berubah?"),
    ],
    "Prinsip 4 — Enabling a Holistic Approach": [
        ("4.1", "Apakah hak akses pengguna diberikan berdasarkan tugas dan prinsip kebutuhan untuk mengetahui?"),
        ("4.2", "Apakah aktivitas penting, perubahan, dan akses istimewa dicatat dalam log serta ditinjau secara berkala?"),
        ("4.3", "Apakah pencadangan data dilakukan sesuai jadwal dan hasil pemulihannya diuji?"),
        ("4.4", "Apakah tersedia prosedur penanganan insiden dan pemulihan layanan saat sistem terganggu?"),
        ("4.5", "Apakah personel memperoleh pelatihan terkait keamanan informasi, privasi, dan prosedur kerja sistem?"),
        ("4.6", "Apakah kualitas dan konsistensi data transaksi dipantau untuk mengurangi kesalahan atau duplikasi?"),
    ],
    "Prinsip 5 — Separating Governance from Management": [
        ("5.1", "Apakah pihak yang berwenang menetapkan arah dan kebijakan tata kelola TI telah ditentukan?"),
        ("5.2", "Apakah pelaksana/manajemen TI memiliki tanggung jawab yang jelas untuk menjalankan kebijakan tersebut?"),
        ("5.3", "Apakah kinerja, risiko, insiden, dan kepatuhan TI dilaporkan kepada pihak pengawas atau pimpinan secara berkala?"),
        ("5.4", "Apakah temuan audit atau evaluasi sebelumnya memiliki penanggung jawab dan tenggat penyelesaian?"),
        ("5.5", "Apakah pimpinan meninjau hasil pengukuran dan menetapkan tindakan perbaikan jika target tidak tercapai?"),
    ],
}

REFERENCES = [
    "Dwi, R., Astriyani, E., Salsabila, F., Fitriani, H., & Gracia, G. (2025). Audit Sistem Informasi Terhadap Sistem Pembelian di Aplikasi Shopee Menggunakan Framework COBIT 5. Journal CERITA: Creative Education of Research in Information Technology and Artificial Informatics, 11(1), 103–111. https://doi.org/10.33050/cerita.v11i1.3714",
    "Muhamad, R., H, Z. N., Astuti, K., Fadhli, M., & Fahlapi, R. (2024). Audit Tata Kelola Sistem Informasi Aplikasi Shopee Menggunakan Framework COBIT 5. HUMANITIS: Jurnal Humaniora, Sosial dan Bisnis, 2(6), 690–698. https://humanisa.my.id/index.php/hms/article/view/181",
    "Wahyuni, T., & Hidayah, N. (2026). Analisis Kualitas Layanan TI Menggunakan Framework COBIT 5 pada Aplikasi Shopee (Studi Kasus: Mahasiswa Universitas Riau). TEKNOFILE: Jurnal Sistem Informasi, 4(1). https://jurnal.nawansa.com/index.php/teknofile/article/view/595",
    "Aisah, A., Putri, N., Br.Stp, C. N., & Nurhaliza. (2025). Audit Sistem Informasi dalam Meningkatkan Kepuasan Pengguna E-commerce Shopee Menggunakan Metode PIECES Framework. Warta Dharmawangsa, 19(1), 548–558. https://doi.org/10.46576/wdw.v19i1.5932",
    "Sobirin, M. H., & Suryono, R. R. (2025). Audit Tata Kelola Teknologi Informasi untuk Website Pelayanan Terpadu Satu Pintu (PTSP) menggunakan Framework COBIT 5. Dinamik, 30(2), 152–159. https://doi.org/10.35315/dinamik.v30i2.10138",
]

ALL_QUESTIONS = [(principle, qid, question) for principle, items in PRINCIPLES.items() for qid, question in items]

if "audit_answers" not in st.session_state:
    st.session_state.audit_answers = {
        qid: {"score": "N/A", "evidence": "", "recommendation": ""}
        for _, qid, _ in ALL_QUESTIONS
    }

if "audit_identity" not in st.session_state:
    st.session_state.audit_identity = {
        "auditor": "Zaki Wahyu Rijal Maulana",
        "date": "",
        "unit": "Sistem Informasi E-Commerce",
        "source": "",
        "documents": "",
    }

def get_results():
    assessed = []
    for principle, qid, question in ALL_QUESTIONS:
        answer = st.session_state.audit_answers[qid]
        score = answer["score"]
        if score != "N/A":
            assessed.append({
                "Prinsip": principle,
                "No.": qid,
                "Pertanyaan Audit": question,
                "Skor": int(score),
                "Bukti/Catatan": answer["evidence"],
                "Rekomendasi": answer["recommendation"],
            })
    total = sum(row["Skor"] for row in assessed)
    maximum = len(assessed) * 3
    percentage = (total / maximum * 100) if maximum else 0
    return assessed, total, maximum, percentage

def category_for(pct):
    if pct < 40:
        return "Perlu perbaikan prioritas"
    if pct < 60:
        return "Pengendalian masih lemah"
    if pct < 80:
        return "Cukup, tetapi perlu peningkatan"
    return "Baik berdasarkan bukti yang diperiksa"

# =========================
# SIDEBAR
# =========================
with st.sidebar:
    st.title("🛒 COBIT 5 E-Commerce")
    st.caption("Aplikasi Form Audit Sistem Informasi")
    page = st.radio(
        "Navigasi",
        ["Beranda", "Profil Audit", "Form Audit", "Hasil Audit", "Tentang & Pustaka"],
        label_visibility="collapsed"
    )
    st.divider()
    st.caption("Tugas AUSI — Universitas Muria Kudus")
    st.caption("Zaki Wahyu Rijal Maulana")

# =========================
# BERANDA
# =========================
if page == "Beranda":
    st.title("Audit Sistem Informasi E-Commerce")
    st.subheader("Menggunakan Kerangka Kerja COBIT 5")
    st.write(
        "Aplikasi ini merupakan implementasi digital dari form audit pada Tugas 1 "
        "Audit dan Tata Kelola Sistem Informasi (AUSI). Objek studi kasus akademik "
        "yang digunakan adalah sistem informasi pada PT Shopee Indonesia."
    )
    st.info(
        "Catatan: form ini merupakan instrumen akademik. Aplikasi tidak menyatakan "
        "bahwa audit resmi telah dilakukan pada PT Shopee Indonesia. Setiap skor "
        "harus didasarkan pada bukti yang diperoleh auditor."
    )
    assessed, total, maximum, pct = get_results()
    c1, c2, c3 = st.columns(3)
    c1.metric("Jumlah pertanyaan", len(ALL_QUESTIONS))
    c2.metric("Sudah dinilai", len(assessed))
    c3.metric("Persentase sementara", f"{pct:.1f}%")
    st.markdown("### Lima Prinsip COBIT 5")
    descriptions = [
        ("1. Meeting Stakeholder Needs", "Memenuhi kebutuhan pemangku kepentingan dengan mempertimbangkan manfaat, risiko, dan sumber daya."),
        ("2. Covering the Enterprise End-to-End", "Mencakup seluruh organisasi, proses bisnis, fungsi pendukung, dan pihak eksternal yang relevan."),
        ("3. Applying a Single Integrated Framework", "Mengintegrasikan berbagai standar, kebijakan, dan praktik tata kelola TI."),
        ("4. Enabling a Holistic Approach", "Memperhatikan proses, struktur organisasi, budaya, informasi, layanan, dan kompetensi."),
        ("5. Separating Governance from Management", "Memisahkan penetapan arah dan pengawasan dari pelaksanaan aktivitas manajemen."),
    ]
    for title, desc in descriptions:
        with st.container(border=True):
            st.markdown(f"**{title}**")
            st.write(desc)
    st.markdown("### Cara menggunakan aplikasi")
    st.write("1. Lengkapi identitas pelaksanaan audit pada menu **Profil Audit**.")
    st.write("2. Isi skor, bukti/catatan, dan rekomendasi pada menu **Form Audit**.")
    st.write("3. Buka **Hasil Audit** untuk melihat perhitungan otomatis dan mengunduh rekap CSV.")

# =========================
# PROFIL AUDIT
# =========================
elif page == "Profil Audit":
    st.title("Identitas Pelaksanaan Audit")
    st.write("Lengkapi informasi pelaksanaan audit. Tanda (-) dapat digunakan jika data belum tersedia.")
    identity = st.session_state.audit_identity
    with st.form("identity_form"):
        auditor = st.text_input("Nama auditor", value=identity["auditor"])
        date = st.text_input("Tanggal audit", value=identity["date"], placeholder="Contoh: 16 November 2026")
        unit = st.text_input("Unit/proses yang diperiksa", value=identity["unit"])
        source = st.text_input("Narasumber", value=identity["source"], placeholder="-")
        documents = st.text_area("Dokumen/bukti yang diperiksa", value=identity["documents"], placeholder="Tuliskan dokumen atau bukti yang diperiksa...")
        submitted = st.form_submit_button("Simpan Identitas", type="primary")
        if submitted:
            st.session_state.audit_identity = {
                "auditor": auditor, "date": date, "unit": unit,
                "source": source, "documents": documents
            }
            st.success("Identitas audit berhasil disimpan pada sesi aplikasi ini.")
    st.markdown("### Objek dan ruang lingkup")
    st.write(
        "Objek studi kasus adalah sistem informasi pada perusahaan e-commerce PT Shopee Indonesia, "
        "khususnya layanan digital yang mendukung aktivitas pengguna dan transaksi. Area perhatian "
        "meliputi pengelolaan akun, katalog produk, proses pesanan, pembayaran, layanan pelanggan, "
        "ketersediaan aplikasi, pengelolaan data, serta koordinasi dengan penjual dan penyedia jasa pengiriman."
    )

# =========================
# FORM AUDIT
# =========================
elif page == "Form Audit":
    st.title("Form Audit Berbasis Lima Prinsip COBIT 5")
    st.write("Pilih skor untuk setiap pertanyaan. Isi bukti/catatan dan rekomendasi berdasarkan hasil pemeriksaan.")
    with st.expander("Petunjuk pengisian dan skala penilaian", expanded=True):
        st.markdown("""
        - **0** = Tidak ada/belum diterapkan
        - **1** = Diterapkan secara terbatas atau ad hoc
        - **2** = Diterapkan sebagian
        - **3** = Diterapkan secara konsisten dan terdokumentasi
        - **N/A** = Tidak relevan dengan ruang lingkup

        Skala ini merupakan skala sederhana untuk tugas akademik, bukan penilaian kapabilitas resmi COBIT.
        Skor tidak boleh diberikan hanya berdasarkan asumsi.
        """)
    for principle, items in PRINCIPLES.items():
        with st.expander(principle, expanded=False):
            for qid, question in items:
                answer = st.session_state.audit_answers[qid]
                st.markdown(f"**{qid}. {question}**")
                col1, col2 = st.columns([1, 2])
                with col1:
                    selected = st.selectbox(
                        "Skor",
                        ["N/A", "0", "1", "2", "3"],
                        index=["N/A", "0", "1", "2", "3"].index(answer["score"]),
                        key=f"score_{qid}"
                    )
                with col2:
                    evidence = st.text_input(
                        "Bukti/catatan",
                        value=answer["evidence"],
                        key=f"evidence_{qid}",
                        placeholder="Catat bukti yang diperiksa..."
                    )
                recommendation = st.text_area(
                    "Rekomendasi",
                    value=answer["recommendation"],
                    key=f"recommendation_{qid}",
                    placeholder="Tuliskan rekomendasi perbaikan...",
                    height=70
                )
                st.session_state.audit_answers[qid] = {
                    "score": selected,
                    "evidence": evidence,
                    "recommendation": recommendation
                }
                st.divider()
    assessed, total, maximum, pct = get_results()
    st.metric("Pertanyaan yang sudah dinilai", f"{len(assessed)} dari {len(ALL_QUESTIONS)}")
    st.progress(len(assessed) / len(ALL_QUESTIONS))
    st.caption("Jawaban tersimpan sementara selama sesi aplikasi aktif. Unduh rekap pada menu Hasil Audit agar tidak hilang.")

# =========================
# HASIL AUDIT
# =========================
elif page == "Hasil Audit":
    st.title("Pengolahan dan Ringkasan Hasil Audit")
    assessed, total, maximum, pct = get_results()
    identity = st.session_state.audit_identity
    st.markdown("### Identitas audit")
    st.write(f"**Auditor:** {identity['auditor'] or '-'}")
    st.write(f"**Tanggal audit:** {identity['date'] or '-'}")
    st.write(f"**Unit/proses:** {identity['unit'] or '-'}")
    st.write(f"**Narasumber:** {identity['source'] or '-'}")
    st.write(f"**Dokumen/bukti:** {identity['documents'] or '-'}")
    st.divider()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Butir dinilai", len(assessed))
    c2.metric("Total skor", total)
    c3.metric("Skor maksimum", maximum)
    c4.metric("Persentase", f"{pct:.1f}%")
    st.subheader("Interpretasi sementara")
    st.progress(int(round(pct)))
    st.markdown(f"**{category_for(pct) if assessed else 'Belum ada penilaian'}**")
    st.caption("Kategori interpretasi latihan: 0–39% perlu perbaikan prioritas; 40–59% pengendalian masih lemah; 60–79% cukup, tetapi perlu peningkatan; 80–100% baik berdasarkan bukti yang diperiksa.")
    if not assessed:
        st.warning("Belum ada pertanyaan yang diberi skor. Silakan isi Form Audit terlebih dahulu.")
    else:
        st.markdown("### Rekap per prinsip")
        rows = []
        for principle in PRINCIPLES:
            p_rows = [r for r in assessed if r["Prinsip"] == principle]
            p_total = sum(r["Skor"] for r in p_rows)
            p_max = len(p_rows) * 3
            p_pct = (p_total / p_max * 100) if p_max else 0
            rows.append({
                "Prinsip": principle,
                "Butir dinilai": len(p_rows),
                "Total skor": p_total,
                "Skor maksimum": p_max,
                "Persentase": f"{p_pct:.1f}%"
            })
        df_summary = pd.DataFrame(rows)
        st.dataframe(df_summary, use_container_width=True, hide_index=True)
        st.markdown("### Detail jawaban")
        df_detail = pd.DataFrame(assessed)
        st.dataframe(df_detail, use_container_width=True, hide_index=True)
        csv = df_detail.to_csv(index=False).encode("utf-8-sig")
        st.download_button(
            "⬇️ Unduh Rekap Audit (CSV)",
            data=csv,
            file_name="rekap_audit_cobit5_ecommerce.csv",
            mime="text/csv",
            type="primary"
        )
    st.info(
        "Persentase dihitung dengan rumus: (total skor yang diperoleh ÷ total skor maksimum "
        "dari butir yang dinilai) × 100%. Butir N/A dikeluarkan dari perhitungan. "
        "Hasil harus disertai bukti, risiko, dan konteks; bukan jaminan bahwa sistem sepenuhnya aman."
    )

# =========================
# TENTANG & PUSTAKA
# =========================
elif page == "Tentang & Pustaka":
    st.title("Tentang Aplikasi")
    st.write(
        "Aplikasi ini dibuat sebagai pengembangan digital dari dokumen "
        "“Form Audit Sistem Informasi pada Perusahaan E-Commerce Menggunakan Kerangka Kerja COBIT 5”."
    )
    st.markdown("### Informasi penyusun")
    st.write("**Nama:** Zaki Wahyu Rijal Maulana")
    st.write("**NIM:** 202453045")
    st.write("**Program Studi:** Sistem Informasi")
    st.write("**Fakultas:** Teknik")
    st.write("**Universitas:** Universitas Muria Kudus")
    st.write("**Dosen Pengampu:** Dr. Ir. Arif Setiawan, S.Kom., M.Cs., IPM")
    st.markdown("### Batasan aplikasi")
    st.write(
        "Form ini merupakan rancangan instrumen akademik. Tidak dilakukan pengujian teknis, "
        "wawancara dengan pihak perusahaan, verifikasi dokumen internal, atau pengukuran tingkat "
        "kapabilitas resmi. Penilaian hanya bermakna jika skor didasarkan pada bukti yang sah."
    )
    st.markdown("### Daftar Pustaka")
    for ref in REFERENCES:
        st.write(ref)
    st.caption("Sumber isi: dokumen Tugas 1 AUSI yang diberikan pengguna.")

st.sidebar.divider()
st.sidebar.caption("COBIT 5 • E-Commerce • AUSI 2026")

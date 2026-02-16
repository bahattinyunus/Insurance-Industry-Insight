import streamlit as st
import pandas as pd
import datetime

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Vet. Med. Çalışma Asistanı",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel Stil
st.markdown("""
    <style>
        .main {
            background-color: #f9f9f9;
        }
        .stButton>button {
            color: #ffffff;
            background-color: #2e8b57; /* SeaGreen for medical feel */
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

# Kenar Çubuğu
with st.sidebar:
    st.image("https://img.icons8.com/color/96/ios-glyphs/veterinarian.png", width=80)
    st.title("🐾 Vet. Öğrenci Asistanı")
    st.markdown("---")
    st.markdown("### Çalışma Modülleri")
    page = st.radio("Git", ["Genel Bakış", "Ders Notları", "Vaka Analizleri", "Sözlük & Referans"])
    st.markdown("---")
    st.info("⚠️ Bu uygulama sadece eğitim amaçlıdır. Tıbbi tanı/tedavi için kullanılamaz.")

# Ana İçerik
if page == "Genel Bakış":
    st.title("🩺 Hoşgeldin, Hekim Adayı")
    st.markdown("Bugün hangi konuya odaklanıyoruz? Unutma, **işin ucunda hayat var.**")

    # İlerleme Kartları
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Tamamlanan Konular", value="12", delta="2 (Bu Hafta)")
    with col2:
        st.metric(label="Çözülen Vaka (Teorik)", value="5")
    with col3:
        st.metric(label="Sıradaki Sınav", value="Anatomi II", delta="3 Gün Kaldı", delta_color="inverse")

    st.markdown("### 📅 Haftalık Çalışma Programı")
    study_plan = pd.DataFrame({
        'Gün': ['Pazartesi', 'Salı', 'Çarşamba', 'Perşembe', 'Cuma'],
        'Sabah': ['Anatomi (Osteoloji)', 'Fizyoloji (Sinir Sis.)', 'Histoloji', 'Anatomi (Miyoloji)', 'Klinik Bilimler'],
        'Öğleden Sonra': ['Biyokimya', 'Farmakoloji', 'Patoloji', 'Vaka Analizi', 'Yabancı Dil']
    })
    st.table(study_plan)

elif page == "Ders Notları":
    st.title("📚 Ders Notları Arşivi")
    subject = st.selectbox("Ders Seçiniz:", ["Anatomi", "Fizyoloji", "Biyokimya", "Farmakoloji", "İç Hastalıkları"])
    
    st.markdown(f"### {subject} Notları")
    st.write("Bu alanda Markdown formatındaki ders notlarınız görüntülenecektir.")
    
    if subject == "Anatomi":
        with st.expander("Osteoloji (Kemik Bilimi) - Özet"):
            st.markdown("- **Axial İskelet:** Kafatası, omurga, kaburgalar, sternum.\n- **Appendicular İskelet:** Ön ve arka ekstremiteler.")

elif page == "Vaka Analizleri":
    st.title("🔬 Teorik Vaka İncelemeleri")
    st.write("Burada anonimleştirilmiş veya kurgusal vakalar üzerinden tanısal yaklaşım pratiği yapılır.")
    
    st.info("Vaka No: #2024-001 | Tür: Felis catus (Kedi) | Şikayet: İştahsızlık ve Letarji")
    
    approach = st.text_area("Ayırıcı Tanı Yaklaşımınız:", placeholder="Semptomları ve olası nedenleri buraya not alın...")
    if st.button("Notu Kaydet"):
        st.success("Analiz notunuz veritabanına kaydedildi.")

elif page == "Sözlük & Referans":
    st.title("📖 Terminoloji ve Referans Değerler")
    st.text_input("Terim Ara:", placeholder="Örn: Taşikardi, Diskezi...")
    
    st.markdown("### Hemogram Referans Aralıkları (Kedi/Köpek)")
    st.warning("Referans değerleri laboratuvara ve cihaza göre değişebilir.")
    # Örnek Tablo
    ref_data = pd.DataFrame({
        'Parametre': ['RBC', 'WBC', 'HCT', 'PLT'],
        'Köpek': ['5.5-8.5', '6-17', '37-55', '200-500'],
        'Kedi': ['5-10', '5.5-19.5', '24-45', '300-800']
    })
    st.dataframe(ref_data, use_container_width=True)

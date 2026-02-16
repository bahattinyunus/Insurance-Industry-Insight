import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Sayfa Yapılandırması
st.set_page_config(
    page_title="Sigorta Endüstrisi İçgörüleri",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Özel Stil
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            color: #ffffff;
            background-color: #ff4b4b;
            border-radius: 10px;
        }
    </style>
""", unsafe_allow_html=True)

# Kenar Çubuğu
with st.sidebar:
    st.title("🛡️ Sigorta İçgörü")
    st.markdown("---")
    st.markdown("### Navigasyon")
    page = st.radio("Git", ["Panel", "Veri Kaşifi", "YZ Modelleri", "Ayarlar"])
    st.markdown("---")
    st.markdown("v0.1.0 | Alfa")

# Ana İçerik
if page == "Panel":
    st.title("📊 Yönetici Paneli")
    st.markdown("Sigorta piyasası trendlerine ve portföy performansına dair gerçek zamanlı içgörüler.")

    # Temel Metrikler Satırı
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric(label="Toplam Yazılan Prim (GWP)", value="₺12.5M", delta="%8.2")
    with col2:
        st.metric(label="Hasar Oranı (Loss Ratio)", value="%62.4", delta="-%1.5", delta_color="inverse")
    with col3:
        st.metric(label="Aktif Poliçeler", value="15,402", delta="124")
    with col4:
        st.metric(label="Müşteri Tutma", value="%94.2", delta="%0.3")

    st.markdown("---")

    # Örnek Grafikler
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Aylık Prim Trendi")
        # Örnek Veri
        df_trend = pd.DataFrame({
            'Ay': pd.date_range(start='2024-01-01', periods=6, freq='M'),
            'Prim': np.random.randint(1000000, 2000000, 6)
        })
        fig_trend = px.line(df_trend, x='Ay', y='Prim', markers=True, template="plotly_white")
        st.plotly_chart(fig_trend, use_container_width=True)

    with col_right:
        st.subheader("Portföy Dağılımı")
        # Örnek Veri
        df_dist = pd.DataFrame({
            'Segment': ['Oto', 'Sağlık', 'Konut', 'Hayat', 'Ticari'],
            'Değer': [35, 25, 20, 10, 10]
        })
        fig_dist = px.pie(df_dist, values='Değer', names='Segment', hole=0.4, template="plotly_white")
        st.plotly_chart(fig_dist, use_container_width=True)

elif page == "Veri Kaşifi":
    st.title("💾 Veri Kaşifi")
    st.warning("Keşfetmeye başlamak için veri kaynağınızı bağlayın.")

elif page == "YZ Modelleri":
    st.title("🤖 YZ Risk Değerlendirmesi")
    st.info("Tahminleyici modeller çok yakında.")

elif page == "Ayarlar":
    st.title("⚙️ Ayarlar")
    st.checkbox("Karanlık Modu Etkinleştir")
    st.checkbox("Geliştirici Araçlarını Göster")

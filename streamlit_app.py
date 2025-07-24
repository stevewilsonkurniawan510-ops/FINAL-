import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Angka", page_icon="🎯")

st.title("🎯 GAME TEBAK ANGKA 👌")

# Inisialisasi session state
if "level" not in st.session_state:
    st.session_state.level = 1
if "maxlevel" not in st.session_state:
    st.session_state.maxlevel = 50
if "batas" not in st.session_state:
    st.session_state.batas = st.session_state.level * 5
if "angkarandom" not in st.session_state:
    st.session_state.angkarandom = random.randint(1, st.session_state.batas)
if "jumlahtebakan" not in st.session_state:
    st.session_state.jumlahtebakan = 0
if "makstebakan" not in st.session_state:
    st.session_state.makstebakan = 5 + ((st.session_state.level - 1) // 2)
if "pesan" not in st.session_state:
    st.session_state.pesan = ""

st.subheader(f"📈 LEVEL {st.session_state.level}")
st.write(f"Tebak angka dari 1 sampai {st.session_state.batas}")
st.write(f"🎯 Kesempatan kamu: {st.session_state.makstebakan - st.session_state.jumlahtebakan}x")

tebakan = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=st.session_state.batas, step=1)

tombol = st.button("Tebak!")

if tombol:
    st.session_state.jumlahtebakan += 1
    
    if tebakan < st.session_state.angkarandom:
        st.session_state.pesan = "⬇️ Tebakanmu terlalu kecil ❌"
    elif tebakan > st.session_state.angkarandom:
        st.session_state.pesan = "⬆️ Tebakanmu terlalu besar ❌"
    else:
        st.success("✅ Yeay Benar!")
        st.session_state.level += 1
        if st.session_state.level > st.session_state.maxlevel:
            st.balloons()
            st.success("🎉 SELAMAT! Kamu telah menyelesaikan semua level 🎉")
            st.stop()
        st.session_state.batas = st.session_state.level * 5
        st.session_state.angkarandom = random.randint(1, st.session_state.batas)
        st.session_state.jumlahtebakan = 0
        st.session_state.makstebakan = 5 + ((st.session_state.level - 1) // 2)
        st.rerun()

    if st.session_state.jumlahtebakan >= st.session_state.makstebakan:
        st.error(f"\n❌ Kamu gagal! Angka yang benar adalah {st.session_state.angkarandom}")
        st.warning("💀 GAME OVER 💀")
        if st.button("🔁 Mulai Lagi"):
            for key in st.session_state.keys():
                del st.session_state[key]
            st.rerun()

if st.session_state.pesan:
    st.info(st.session_state.pesan)

st.markdown("""
---
👨‍💻 Developer: Steve  
📢 Jangan lupa beri tanggapan, kami akan update! 🔧
""")

import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Angka", page_icon="🎯")

# Inisialisasi state
if "level" not in st.session_state:
    st.session_state.level = 1
    st.session_state.max_level = 10
    st.session_state.batas = 10
    st.session_state.angka_rahasia = random.randint(1, 10)
    st.session_state.jumlah_tebakan = 0
    st.session_state.maks_tebakan = 5
    st.session_state.game_over = False
    st.session_state.menang = False

st.title("🎯 Game Tebak Angka Berlevel")

level = st.session_state.level
batas = level * 10
maks_tebakan = 5 + ((level - 1) // 2)

if st.session_state.batas != batas:
    st.session_state.batas = batas
    st.session_state.angka_rahasia = random.randint(1, batas)
    st.session_state.jumlah_tebakan = 0
    st.session_state.maks_tebakan = maks_tebakan
    st.session_state.game_over = False
    st.session_state.menang = False

st.subheader(f"Level {level}")
st.write(f"Tebak angka dari 1 sampai **{batas}**")
st.write(f"Kesempatan: **{maks_tebakan - st.session_state.jumlah_tebakan}** kali")

if not st.session_state.game_over:
    tebakan = st.number_input("Masukkan tebakanmu:", min_value=1, max_value=batas, step=1)

    if st.button("Tebak"):
        st.session_state.jumlah_tebakan += 1
        if tebakan < st.session_state.angka_rahasia:
            st.warning("Tebakanmu terlalu kecil!")
        elif tebakan > st.session_state.angka_rahasia:
            st.warning("Tebakanmu terlalu besar!")
        else:
            st.success("🎉 Selamat! Kamu benar!")
            st.session_state.menang = True
            st.session_state.game_over = True

        if st.session_state.jumlah_tebakan >= st.session_state.maks_tebakan and not st.session_state.menang:
            st.error(f"💀 Game Over! Angka yang benar adalah {st.session_state.angka_rahasia}")
            st.session_state.game_over = True

# Tombol setelah menang/kalah
if st.session_state.game_over:
    col1, col2 = st.columns(2)
    with col1:
        if st.session_state.menang and level < st.session_state.max_level:
            if st.button("👉 Lanjut ke Level Berikutnya"):
                st.session_state.level += 1
                st.session_state.batas = st.session_state.level * 10
                st.session_state.angka_rahasia = random.randint(1, st.session_state.batas)
                st.session_state.jumlah_tebakan = 0
                st.session_state.maks_tebakan = 5 + ((st.session_state.level - 1) // 2)
                st.session_state.game_over = False
                st.session_state.menang = False
                st.experimental_rerun()
        elif st.session_state.menang and level == st.session_state.max_level:
            st.balloons()
            st.success("🏁 Kamu berhasil menyelesaikan semua level!")

    with col2:
        if st.button("🔁 Mulai dari awal"):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()

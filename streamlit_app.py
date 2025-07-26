import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Angka", page_icon="🎯", layout="centered")
st.title("🎯 GAME TEBAK ANGKA 👌")

# Inisialisasi
if 'level' not in st.session_state:
    st.session_state.level = 1
    st.session_state.maxlevel = 50
    st.session_state.tebakan_ke = 1
    st.session_state.angkarandom = random.randint(1, st.session_state.level * 5)
    st.session_state.skor = 0
    st.session_state.sisa_tebakan = 5 + ((st.session_state.level - 1) // 2)
    st.session_state.game_over = False
    st.session_state.menang = False
    st.session_state.tanya_lanjut = False
    st.session_state.keluar = False

# Fungsi reset awal
def mulai_ulang():
    st.session_state.level = 1
    st.session_state.tebakan_ke = 1
    st.session_state.angkarandom = random.randint(1, 5)
    st.session_state.skor = 0
    st.session_state.sisa_tebakan = 5
    st.session_state.game_over = False
    st.session_state.menang = False
    st.session_state.tanya_lanjut = False
    st.session_state.keluar = False

# Pertanyaan setelah kalah/menang
if st.session_state.tanya_lanjut:
    st.markdown("## 🔁 Mau main lagi dari awal?")
    pilihan = st.radio("Pilih salah satu:", ["Ya", "Tidak"], key="lanjut_main")

    if st.button("Lanjutkan"):
        if pilihan == "Ya":
            mulai_ulang()
        else:
            st.session_state.keluar = True
            st.session_state.tanya_lanjut = False

# Pesan kalau user memilih keluar
elif st.session_state.keluar:
    st.success("Terima kasih telah bermain! Sampai jumpa lagi 👋")
    st.stop()

# Game sedang berjalan
elif not st.session_state.game_over and not st.session_state.menang:

    batas = st.session_state.level * 5
    st.markdown(f"## 📈 Level {st.session_state.level}")
    st.write(f"Tebak angka dari **1 sampai {batas}**")
    st.write(f"🎯 Kesempatan sisa: {st.session_state.sisa_tebakan}")
    tebakan = st.number_input(f"Tebakan ke-{st.session_state.tebakan_ke}", min_value=1, max_value=batas, step=1, key="input")

    if st.button("🚀 Submit Tebakan"):
        if tebakan < st.session_state.angkarandom:
            st.warning("⬇️ Tebakanmu terlalu kecil ❌")
        elif tebakan > st.session_state.angkarandom:
            st.warning("⬆️ Tebakanmu terlalu besar ❌")
        else:
            st.success("✅ Yeay benar!")
            st.session_state.skor += 1
            st.session_state.level += 1
            st.session_state.tebakan_ke = 1
            if st.session_state.level > st.session_state.maxlevel:
                st.session_state.menang = True
            else:
                st.session_state.angkarandom = random.randint(1, st.session_state.level * 5)
                st.session_state.sisa_tebakan = 5 + ((st.session_state.level - 1) // 2)
            st.stop()

        st.session_state.sisa_tebakan -= 1
        st.session_state.tebakan_ke += 1

        if st.session_state.sisa_tebakan <= 0:
            st.session_state.game_over = True
            st.error(f"❌ Kamu gagal! Angka yang benar adalah {st.session_state.angkarandom}")
            st.session_state.tanya_lanjut = True

# Menang
elif st.session_state.menang:
    st.balloons()
    st.success("🎉 SELAMAT! Kamu telah menyelesaikan semua level!")
    st.write(f"Total skor kamu: {st.session_state.skor}")
    st.session_state.tanya_lanjut = True

st.markdown("---")
st.caption("Developer by: Steve 🚀")


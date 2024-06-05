import pandas as pd

df = pd.read_csv('dataset.csv')

# Pisahkan kolom kategori menjadi daftar
df['kategori'] = df['kategori'].str.split(', ')

# Explode kolom kategori
df = df.explode('kategori')

# Pisahkan kolom kategori user menjadi daftar
df['Kategori User'] = df['Kategori User'].str.split(', ')

# Explode kolom kategori user
df = df.explode('Kategori User')

def master_category_user():
    # Mengisi nilai yang hilang dengan string kosong
    df['Kategori User'] = df['Kategori User'].fillna('')

    # Memastikan semua nilai dalam kolom kKategori' adalah string
    df['Kategori User'] = df['Kategori User'].astype(str)

    # Mendapatkan hasil unique kategori diurutkan berdasarkan huruf alfabet
    unique_categories = sorted([kategori for kategori in df['Kategori User'].unique() if kategori])

    return unique_categories

def master_category():
    # Mengisi nilai yang hilang dengan string kosong
    df['kategori'] = df['kategori'].fillna('')

    # Memastikan semua nilai dalam kolom kKategori' adalah string
    df['kategori'] = df['kategori'].astype(str)

    # Mendapatkan hasil unique kategori diurutkan berdasarkan huruf alfabet
    unique_categories = sorted([kategori for kategori in df['kategori'].unique() if kategori])

    return unique_categories

def select_category(category_user, category):
    filtered_df = pd.DataFrame()
    try :
        filtered_df = df[df['Kategori User'] == category_user]
        filtered_df = filtered_df[filtered_df['kategori'] == category].sort_values(by='rating', ascending=False)
    except:
        return "Kategori tidak sesuai"

    return filtered_df
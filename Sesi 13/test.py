import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('data-score.xlsx', sheet_name='TI24E')

df = df.dropna(subset=['Score'])

def kategori_nilai(score):
    if score >= 85:
        return 'A'
    elif score >= 70:
        return 'B'
    elif score >= 60:
        return 'C'
    elif score >= 50:
        return 'D'
    else:
        return 'E'
    
df['Kategori'] = df['Score'].apply(kategori_nilai)

persentase_kategori = (df['Kategori'].value_counts(normalize=True).sort_index()) * 100

plt.figure(figsize=(88, 6))
persentase_kategori.plot(kind='bar', color='skyblue', edgecolor='black')

plt.title('Persentase Mahasiswa per kategori Nilai')
plt.xlabel('Kategori Nilai')
plt.ylabel('Peersentase (%)')
plt.ylim(0,100)
plt.grid(axis='y', linestyle='--', alpha=0.7)

for i, v in enumerate(persentase_kategori):
    plt.text(i, v + 1, f"{v:.1f}%", ha='center')
    
plt.tight_layout()
plt.show()
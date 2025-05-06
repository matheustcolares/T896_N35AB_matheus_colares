# T896_N35AB_matheus_colares
# Processamento de Imagens com OpenCV

Este repositório contém três projetos práticos desenvolvidos com Python e OpenCV, cada um focado em um aspecto específico do processamento de imagens. Os códigos estão organizados por tema e utilizam imagens de entrada localizadas na pasta `img/`.

## 📁 Estrutura do Repositório

```
├── ChromaKey.py
├── Circulos.py
├── PlantaDanificada.py
├── img/
│   ├── projeto1/
│   │   ├── pessoa_fundo_verde.jpg
│   │   └── novo_fundo.jpg
│   ├── projeto2/
│   │   └── circulos_1.png
│   └── projeto3/
│       └── folha.jpg
└── README.md
```

---

## 📌 Projetos

### 🟢 Projeto 1: Chroma Key (`ChromaKey.py`)
Substitui o fundo verde de uma imagem por um novo cenário, utilizando segmentação por cor no espaço HSV.

**Imagens utilizadas**:  
📂 `img/projeto1/img_fundo_verde_3.png`  
📂 `img/projeto1/background_1.png`

**Execução**:
```bash
python ChromaKey.py
```

---

### 🟣 Projeto 2: Detecção de Círculos (`Circulos.py`)
Detecta automaticamente círculos em uma imagem utilizando a Transformada de Hough.

**Imagem utilizada**:  
📂 `img/projeto2/circulos_1.png`

**Execução**:
```bash
python Circulos.py
```

---

### 🌿 Projeto 3: Detecção de Folhas Danificadas (`PlantaDanificada.py`)
Segmenta automaticamente as regiões saudáveis e danificadas de uma folha com base na análise de cor em HSV.

**Imagem utilizada**:  
📂 `img/projeto3/img_folha_4.jpg`

**Execução**:
```bash
python PlantaDanificada.py
```

---

## ✅ Requisitos

Certifique-se de instalar as bibliotecas necessárias:

```bash
pip install opencv-python numpy matplotlib
```

---

## 📸 Resultados

Cada script exibe os resultados em janelas separadas para facilitar a visualização das segmentações e detecções realizadas.

---

## 📄 Licença

Este projeto é de uso educacional e pode ser reutilizado livremente com fins de estudo ou demonstração acadêmica.

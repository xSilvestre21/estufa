# 🌱🔥 Dashboard de Controle de Estufa

Sistema de simulação e monitoramento de uma **estufa térmica**, desenvolvido em **Python**, utilizando **Tkinter** para a interface gráfica e **Matplotlib** para visualização em tempo real da temperatura.

O projeto simula o comportamento de uma estufa com controle de temperatura baseado em **controle ON/OFF com histerese**, incluindo:

- Temperatura da estufa
- Temperatura do aquecedor
- Controle por SetPoint (SP)
- Perturbações do ambiente
- Histórico gráfico em tempo real
- Liga/Desliga do sistema


## 🚀 Funcionalidades

### 🌡️ Monitoramento de Temperatura
O sistema exibe em tempo real:

- Temperatura atual da estufa
- Temperatura do aquecedor
- Estado do sistema


### 🎯 Controle de SetPoint
O usuário pode aumentar ou diminuir a temperatura desejada (SP) através dos botões:

- ➕ Aumentar temperatura
- ➖ Diminuir temperatura

---

### 🔥 Controle Automático de Aquecimento
O sistema utiliza um **controle ON/OFF com histerese**:

- Liga o aquecedor quando:

```text
T ≤ SP - h
```

- Desliga o aquecedor quando:

```text
T ≥ SP + h
```

Onde:

- `SP` = temperatura desejada
- `h` = histerese

Isso evita oscilações excessivas no sistema.

---

### 🌎 Simulação de Perturbação Ambiente
O ambiente sofre alteração automática durante a simulação:

- Temperatura ambiente normal: **25°C**
- Entre os ciclos **50 e 80**:
  - temperatura cai para **20°C**

Isso simula uma perturbação externa no ambiente.

---

### 📈 Gráfico em Tempo Real
O sistema gera gráficos dinâmicos contendo:

- Temperatura da estufa
- Temperatura do aquecedor
- Linha do SetPoint
- Faixa de histerese

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **Tkinter** → Interface gráfica
- **Matplotlib** → Visualização dos gráficos
- **FigureCanvasTkAgg** → Integração do gráfico com Tkinter

---

## 🧠 Lógica de Controle

O projeto utiliza um **controle ON/OFF com histerese**, muito utilizado em sistemas industriais para evitar chaveamento excessivo.

### Regras:

Se a temperatura estiver abaixo do limite:

```python
if T <= (SP-h):
    u = 1
```

O aquecedor é ligado.

---

Se a temperatura ultrapassar o limite superior:

```python
elif T >= (SP+h):
    u = 0
```

O aquecedor é desligado.

---

## 📊 Variáveis Principais

| Variável | Função |
|----------|--------|
| `T` | Temperatura da estufa |
| `T_amb` | Temperatura ambiente |
| `T_aquecedor` | Temperatura do aquecedor |
| `SP` | SetPoint desejado |
| `h` | Faixa de histerese |
| `u` | Estado do aquecedor (0 ou 1) |

---

## 🎓 Objetivo do Projeto

Este projeto foi desenvolvido com fins **acadêmicos**, simulando o funcionamento de uma estufa automatizada utilizando conceitos de:

- Automação Industrial
- Sistemas de Controle
- Controle ON/OFF
- Histerese
- Interfaces Gráficas
- Simulação de Processos

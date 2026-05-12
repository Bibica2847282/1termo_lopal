# 🌐 Arquitetura de Sistemas IoT
**Disciplina:** Introdução à Internet das Coisas  
**Semestre:** 2024.X  

---

## 📖 1. Conteúdo de Sala (Fundamentos)
A arquitetura IoT é geralmente dividida em três ou quatro camadas principais:

1.  **Camada de Percepção (Dispositivos):** Sensores e atuadores que coletam dados e interagem com o mundo físico.
2.  **Camada de Rede (Conectividade):** Protocolos de comunicação (Wi-Fi, Bluetooth, LoRaWAN, MQTT, HTTP) que transportam os dados.
3.  **Camada de Processamento (Middleware):** Onde os dados são filtrados e armazenados (Edge Computing ou Cloud).
4.  **Camada de Aplicação:** Interface com o usuário final (Dashboards, Apps).

---

## 🤖 2. Hardware: Arduino
O **Arduino** é a plataforma de prototipagem eletrônica mais utilizada para aprendizado em IoT.

*   **Modelos comuns:** Uno (básico), Mega (mais pinos), ESP32 (ideal para IoT por ter Wi-Fi/Bluetooth nativo).
*   **Componentes Principais:**
    *   **Pinos Digitais:** Entradas/Saídas (LIGADO/DESLIGADO).
    *   **Pinos Analógicos:** Leitura de sensores (ex: temperatura, luminosidade).
    *   **PWM:** Simulação de saídas analógicas.

---

## 💻 3. Linguagem de Programação: C++ (Firmware)
O Arduino é programado em uma variação de **C++**. O código básico sempre possui duas funções:

```cpp
// Executa uma única vez ao ligar
void setup() {
  pinMode(13, OUTPUT); // Define o pino 13 como saída
}

// Executa em loop infinito
void loop() {
  digitalWrite(13, HIGH); // Liga o LED
  delay(1000);            // Espera 1 segundo
  digitalWrite(13, LOW);  // Desliga o LED
  delay(1000);
}
```

---

## 🐍 4. Linguagem de Programação: Python (Integração)
No ecossistema IoT, o **Python** é usado principalmente para:
1.  **Edge Computing:** Processamento de dados em Raspberry Pi.
2.  **Scripts de Servidor:** Receber dados via protocolo MQTT ou HTTP.
3.  **Análise de Dados:** Bibliotecas como Pandas e Matplotlib para tratar os dados coletados.

**Exemplo Simples (Lendo Porta Serial com Python):**
```python
import serial

# Configura a conexão com o Arduino
conexao = serial.Serial('COM3', 9600)

while True:
    dado = conexao.readline()
    print(f"Valor do Sensor: {dado.decode('utf-8')}")
```

---
## 📝 Notas e Referências
*   [Documentação Oficial Arduino](https://arduino.cc)
*   [Python para IoT - Bibliotecas Úteis](https://pypi.org)

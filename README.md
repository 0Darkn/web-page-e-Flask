1. **Servidor Flask**

   * Serve **uma página HTML** escolhida pelo utilizador
   * Porta configurável na interface Qt

2. **Janela Qt (PyQt5)**

   * Caixa para escolher o ficheiro HTML
   * Caixa para definir a porta do servidor
   * Botões:

     * **Ligar**
     * **Desligar**
     * **Sair**
   * Logs simples no terminal

3. **Página Web**

   * HTML + CSS + JavaScript
   * Animação CSS
   * Texto:

     > **"Welcome. This is a Python test."**

4. **Código todo comentado passo a passo**

5. **Explicação clara no fim**

---

# 1️⃣ Estrutura de pastas

```text
flask_qt_server/
│
├─ servidor_qt_flask.py
│
└─ web/
   ├─ index.html
   ├─ style.css
   └─ script.js
```

---

# 2️⃣ Servidor Flask com Janela Qt

## 📄 `servidor_qt_flask.py`

# 3️⃣ Página Web

## 📄 `web/index.html`
## 📄 `web/style.css`
## 📄 `web/script.js`


# 4️⃣ Como usar

1. Instalar dependências:

```bash
pip install flask pyqt5
```

2. Executar:

```bash
python servidor_qt_flask.py
```

3. Na janela:

   * Escolhe `index.html`
   * Define a porta (ex: 5000)
   * Clica **Ligar**

4. No browser:

```text
http://localhost:5000
```

---

# 5️⃣ Explicação resumida

### 🔹 Qt

* Controla o servidor
* Não bloqueia a interface graças a **threading**
* Permite escolher ficheiros e configurar a porta

### 🔹 Flask

* Serve o HTML escolhido dinamicamente
* Usa `send_from_directory` para carregar CSS e JS

### 🔹 Web

* **HTML** → estrutura
* **CSS** → animações (fade + rotação)
* **JavaScript** → comportamento dinâmico

---

Próximo passo:

* ➕ adicionar **logs num ficheiro**
* ➕ permitir **editar o HTML dentro do Qt**
* ➕ suportar **várias páginas**
* ➕ acrescentar **HTTPS**
* ➕ integrar **XML para configurar a página**



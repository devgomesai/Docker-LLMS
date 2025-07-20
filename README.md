# 🚀 Docker Model Runner Setup Guide

This guide walks you through enabling and using Docker's Model Runner to host LLMs like `llama.cpp` locally.

---

## 📌 Prerequisites

- ✅ Docker Desktop installed (latest version)
- ✅ Docker Desktop Model Runner feature available
- ✅ LLM model downloaded or ready to pull (e.g., `ai/smollm2`)

---

## 🛠️ Step-by-Step Setup

### 1. **Enable Model Runner Feature**

Open Docker Desktop and enable Model Runner:

- Via GUI:

  - Go to **Settings → Features in Development → Model Runner**
  - Enable **TCP Support**
  - Apply & Restart Docker
- Or via CLI:

  ```bash
  docker desktop enable model-runner --tcp 12434
  ```

---

### 2. **Verify Model Runner is Active**

Go to your browser and open:

```
http://localhost:12434/
```

You should see:

> "The service is running."

---

### 3. **Pull and Start a Model**

Pull a model using:

```bash
docker model pull ai/smollm2
```

Then, start the model (if not already):

```bash
docker model run ai/smollm2
```

---

### 4. **List Running Models**

Check running models with:

```bash
docker model ps
```

Example output:

```
MODEL NAME   BACKEND    MODE        LAST USED
ai/smollm2   llama.cpp  completion  2 minutes ago
```

---

### 5. **Interact with the Model**

Use the exposed API endpoint:

```
http://localhost:12434/engines/llama.cpp/v1/chat/completions
```

⚠️ Ensure your client or script targets this endpoint correctly.

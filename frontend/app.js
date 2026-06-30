const API = "http://127.0.0.1:8000";

/* =========================
   UPLOAD PDF
========================= */
async function uploadFile(file) {
    if (!file) {
        alert("Please select a PDF file first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch(`${API}/upload`, {
            method: "POST",
            body: formData
        });

        if (!response.ok) {
            const errText = await response.text();
            throw new Error(errText || "Upload failed");
        }

        const data = await response.json();

        console.log("Upload response:", data);

        document.getElementById("status").innerText =
            `Uploaded: ${data.filename || "Unknown"} | Chunks: ${data.chunks_created || 0}`;

    } catch (err) {
        console.error("Upload error:", err);
        alert("Upload failed. Check backend.");
    }
}


/* =========================
   ASK QUESTION
========================= */
async function askQuestion() {
    const questionEl = document.getElementById("question");
    const question = questionEl ? questionEl.value : "";

    if (!question.trim()) {
        alert("Enter a question first.");
        return;
    }

    document.getElementById("answer").innerText = "Thinking...";

    try {
        const res = await fetch(`${API}/ask`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ question })
        });

        if (!res.ok) {
            const errText = await res.text();
            throw new Error(errText || "Ask request failed");
        }

        const data = await res.json();

        /* ANSWER */
        document.getElementById("answer").innerText =
            data.answer ?? "No answer returned";

        /* CITATIONS */
        document.getElementById("citations").innerText =
            Array.isArray(data.citations)
                ? data.citations.join("\n")
                : "No citations available";

        /* LOGS */
        document.getElementById("logs").innerText =
            Array.isArray(data.logs)
                ? data.logs.join("\n")
                : "No logs available";

    } catch (err) {
        console.error("Ask error:", err);
        document.getElementById("answer").innerText =
            "Error generating answer. Check backend.";
    }
}


/* =========================
   FILE INPUT HOOKS
========================= */
function handleFileSelect(event) {
    const file = event.target.files[0];
    uploadFile(file);
}

function uploadSelectedFile() {
    const file = document.getElementById("fileInput")?.files?.[0];
    uploadFile(file);
}
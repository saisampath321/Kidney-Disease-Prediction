document.addEventListener('DOMContentLoaded', () => {
  console.log('Chatbot script loaded successfully.');
  try {
    const qa = [
      {
        keywords: ["kidney disease", "ckd", "chronic kidney disease"],
        answer: "Chronic kidney disease (CKD) is a long-term condition where the kidneys gradually lose function. It’s often caused by diabetes, hypertension, or genetic factors. Symptoms may include fatigue, swelling, and high blood pressure."
      },
      {
        keywords: ["symptoms of kidney disease", "kidney disease symptoms", "signs of kidney disease"],
        answer: "Symptoms of kidney disease include fatigue, swelling in legs or feet, difficulty urinating, high blood pressure, itchy skin, and shortness of breath. Early stages may have no symptoms."
      },
      {
        keywords: ["prevent kidney disease", "kidney disease prevention", "avoid kidney disease"],
        answer: "To prevent kidney disease, stay hydrated, maintain a low-sodium diet, manage blood pressure and diabetes, exercise regularly, and avoid smoking or excessive alcohol."
      },
      {
        keywords: ["treatment for kidney disease", "kidney disease treatment", "cure kidney disease"],
        answer: "Treatment for kidney disease varies by stage. Options include medications to control symptoms, lifestyle changes, dialysis for advanced cases, or kidney transplantation."
      },
      {
        keywords: ["risk factors", "kidney disease risk", "causes of kidney disease"],
        answer: "Risk factors for kidney disease include diabetes, hypertension, family history, obesity, smoking, and older age."
      },
      {
        keywords: ["kidney stones", "renal calculi", "stone in kidney"],
        answer: "Kidney stones are hard deposits of minerals and salts in the kidneys. Symptoms include severe back or side pain, blood in urine, nausea, and frequent urination. Treatment involves hydration, pain relief, or procedures like lithotripsy."
      },
      {
        keywords: ["acute kidney injury", "aki", "acute renal failure"],
        answer: "Acute kidney injury (AKI) is a sudden loss of kidney function, often due to dehydration, infection, or medication side effects. Symptoms include reduced urine output, swelling, and fatigue. Treatment focuses on addressing the underlying cause and may include hospitalization."
      },
      {
        keywords: ["polycystic kidney disease", "pkd", "cysts in kidney"],
        answer: "Polycystic kidney disease (PKD) is a genetic disorder causing fluid-filled cysts to grow in the kidneys, leading to kidney enlargement and reduced function. Symptoms include pain, high blood pressure, and blood in urine. Management includes blood pressure control and monitoring."
      },
      {
        keywords: ["kidney infection", "pyelonephritis", "renal infection"],
        answer: "A kidney infection (pyelonephritis) is a bacterial infection of the kidneys, often following a urinary tract infection. Symptoms include fever, chills, back pain, and painful urination. Treatment typically involves antibiotics and hydration."
      },
      {
        keywords: ["glomerulonephritis", "glomerular disease", "kidney inflammation"],
        answer: "Glomerulonephritis is inflammation of the kidney’s filtering units (glomeruli), often caused by infections, autoimmune diseases, or diabetes. Symptoms include blood in urine, swelling, and high blood pressure. Treatment may involve medications and dietary changes."
      },
      {
        keywords: ["nephrotic syndrome", "kidney syndrome", "protein in urine"],
        answer: "Nephrotic syndrome is a kidney disorder causing excessive protein loss in urine, leading to swelling, low blood protein, and high cholesterol. It can be caused by diabetes, lupus, or infections. Treatment includes medications like steroids and dietary management."
      },
      {
        keywords: ["dialysis", "hemodialysis", "peritoneal dialysis"],
        answer: "Dialysis is a treatment for advanced kidney failure, where a machine filters waste and excess fluid from the blood. Types include hemodialysis (using a machine) and peritoneal dialysis (using the abdominal lining). It’s typically needed when kidney function drops below 10-15%."
      },
      {
        keywords: ["kidney transplant", "renal transplant", "kidney replacement"],
        answer: "A kidney transplant involves surgically replacing a failed kidney with a healthy one from a donor. It’s a treatment for end-stage kidney disease. Patients need lifelong immunosuppressive drugs to prevent rejection."
      },
      {
        keywords: ["diet for kidney health", "kidney diet", "food for kidney"],
        answer: "A kidney-friendly diet includes low-sodium, low-potassium, and low-phosphorus foods. Focus on fresh fruits like apples and berries, vegetables like cabbage, and lean proteins. Avoid processed foods, high-sodium snacks, and excessive protein."
      },
      {
        keywords: ["hydration for kidney", "water for kidney", "drinking water kidney"],
        answer: "Staying hydrated is crucial for kidney health. Drinking 1.5-2 liters of water daily helps the kidneys flush out toxins and prevent stones. However, those with kidney disease may need to limit fluid intake as advised by a doctor."
      }
    ];

    window.toggleChatbot = function() {
      try {
        const chatbot = document.getElementById('chatbot');
        if (!chatbot) throw new Error('Chatbot container not found.');
        chatbot.style.display = chatbot.style.display === 'block' ? 'none' : 'block';
        console.log('Chatbot toggled:', chatbot.style.display);
      } catch (error) {
        console.error('Error in toggleChatbot:', error);
      }
    };

    window.sendMessage = function() {
      try {
        const input = document.getElementById('chatbot-input');
        const messages = document.getElementById('chatbot-messages');
        if (!input || !messages) throw new Error('Chatbot input or messages container not found.');
        
        const userMessage = input.value.trim().toLowerCase();
        if (!userMessage) {
          console.warn('Empty message ignored.');
          return;
        }

        // Add user message
        const userDiv = document.createElement('p');
        userDiv.innerHTML = `<strong>You:</strong> ${userMessage}`;
        messages.appendChild(userDiv);

        // Find response
        let response = "Sorry, I don't understand. Try asking about kidney disease, kidney stones, acute kidney injury, polycystic kidney disease, kidney infection, glomerulonephritis, nephrotic syndrome, dialysis, kidney transplant, diet, hydration, symptoms, prevention, or treatment.";
        for (let qaPair of qa) {
          if (qaPair.keywords.some(keyword => userMessage.includes(keyword.toLowerCase()))) {
            response = qaPair.answer;
            break;
          }
        }

        // Add bot response
        const botDiv = document.createElement('p');
        botDiv.innerHTML = `<strong>Bot:</strong> ${response}`;
        messages.appendChild(botDiv);

        // Clear input and scroll to bottom
        input.value = '';
        messages.scrollTop = messages.scrollHeight;
        console.log('Message sent:', userMessage, 'Response:', response);
      } catch (error) {
        console.error('Error in sendMessage:', error);
      }
    };
  } catch (error) {
    console.error('Error initializing chatbot:', error);
  }
});
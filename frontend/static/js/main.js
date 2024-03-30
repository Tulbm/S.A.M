const sentences = [
    "Struggling with insomnia.",
    "Finding it hard to stay motivated.",
    "Dealing with workplace stress.",
    "Seeking to boost self-confidence.",
    "Experiencing relationship conflicts.",
    "Concerned about weight management.",
    "Feeling down today.",
    "Difficulty concentrating and need assistance.",
    "On a quest for happiness."
];

let currentSentenceIndex = 0;
let currentLetterIndex = 0;
let typingSpeed = 50; // Adjust typing speed as needed
let typingTimeout;

function typeSentence() {
    const currentSentence = sentences[currentSentenceIndex];
    const inputElement = document.getElementById('custom_prompt');

    if (currentLetterIndex < currentSentence.length) {
        inputElement.value += currentSentence.charAt(currentLetterIndex);
        currentLetterIndex++;
        typingTimeout = setTimeout(typeSentence, typingSpeed);
    } else {
        setTimeout(backspace, 1000);

        function backspace() {
            if (currentLetterIndex > 0) {
                inputElement.value = inputElement.value.slice(0, -1);
                currentLetterIndex--;
                setTimeout(backspace, typingSpeed);
            } else {
                currentSentenceIndex = (currentSentenceIndex + 1) % sentences.length;
                currentLetterIndex = 0;
                inputElement.value = "";
                setTimeout(typeSentence, 1000);
            }
        }
    }
}

function stopTyping() {
    clearTimeout(typingTimeout);
    document.getElementById('custom_prompt').value = "";
}

document.getElementById('custom_prompt').addEventListener('click', stopTyping);

typeSentence();



//

let currentQuestion = 1;
const totalQuestions = 2;

function showQuestion() {
    const currentQuestionElement = document.getElementById(`question${currentQuestion}`);
    currentQuestionElement.style.display = "flex";
    currentQuestionElement.style.transform = "translateY(0)";
}

function nextQuestion() {
    const currentQuestionElement = document.getElementById(`question${currentQuestion}`);
    currentQuestionElement.style.display = "none"; // Hide current question
    currentQuestionElement.style.transform = "translateY(-300%)";
    currentQuestion++; // Move to the next question

    if (currentQuestion > totalQuestions) {
        alert('ok');
        return; 
    }

    setTimeout(() => {
        showQuestion();
        updateProgressBar();
    }, 500);
}

// Call showQuestion() to display the first question when the script runs
showQuestion();

function updateProgressBar() {
    const progress = (currentQuestion / totalQuestions) * 100;
    document.getElementById("progress").style.width = `${progress}%`;
}
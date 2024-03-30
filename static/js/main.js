function showError(message) {
    $('.error-message').html(message);
    $('#errorModal').modal('show');
}

function showSuccess(message) {
    $('.success-message').html(message);
    $('#successModal').modal('show');
}

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
    const placeholderElement = document.getElementById('custom_prompt');

    if (currentLetterIndex < currentSentence.length) {
        placeholderElement.setAttribute('placeholder', 
            (placeholderElement.getAttribute('placeholder') || '') + currentSentence.charAt(currentLetterIndex));
        currentLetterIndex++;
        typingTimeout = setTimeout(typeSentence, typingSpeed);
    } else {
        setTimeout(backspace, 1000);

        function backspace() {
            const currentPlaceholder = placeholderElement.getAttribute('placeholder') || '';
            if (currentLetterIndex > 0) {
                placeholderElement.setAttribute('placeholder', currentPlaceholder.slice(0, -1));
                currentLetterIndex--;
                setTimeout(backspace, typingSpeed);
            } else {
                currentSentenceIndex = (currentSentenceIndex + 1) % sentences.length;
                currentLetterIndex = 0;
                placeholderElement.setAttribute('placeholder', '');
                setTimeout(typeSentence, 1000);
            }
        }
    }
}


function stopTyping() {
    clearTimeout(typingTimeout);
    document.getElementById('custom_prompt').setAttribute('placeholder', '');;
}

document.getElementById('custom_prompt').addEventListener('click', stopTyping);

typeSentence();



//

let currentQuestion = 1;
const totalQuestions = 4;
let custom_prompt = document.getElementById('custom_prompt').value;
console.log(custom_prompt);

function showQuestion() {
    const currentQuestionElement = document.getElementById(`question${currentQuestion}`);
    currentQuestionElement.style.display = "flex";
    currentQuestionElement.style.transform = "translateY(0)";
}

function showCompletion(){
    const currentQuestionElement = document.getElementById('completion');
    currentQuestionElement.style.display = "flex";
}

function nextQuestion() {
    const currentQuestionElement = document.getElementById(`question${currentQuestion}`);
    currentQuestionElement.style.display = "none"; 
    currentQuestionElement.style.transform = "translateY(-300%)";
    currentQuestion++; 

    if (currentQuestion > totalQuestions) {
        showCompletion();
    }
    if (custom_prompt === undefined) {
        showError("Prompt is Empty!");
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
document.addEventListener('DOMContentLoaded', () => {
    const outputElement = document.getElementById('output');
    const inputElement = document.getElementById('input');
    const promptElement = document.querySelector('.prompt');

    const items = ['item1', 'item2', 'item3'];

    // Display user prompt
    promptElement.innerHTML = 'guest@hacker:~$ <span class="input" id="input" contenteditable></span>';
    const inputField = document.getElementById('input');

    inputField.focus();

    // Handle user input
    inputField.addEventListener('keydown', (event) => {
        if (event.key === 'Enter') {
            const inputText = inputField.textContent.trim();
            outputElement.innerHTML += `<div class="command-line">guest@hacker:~$ ${inputText}</div>`;

            if (inputText === '1' || inputText === '2' || inputText === '3') {
                const selectedItem = items[parseInt(inputText) - 1];
                outputElement.innerHTML += `<div class="command-line">Opening link for ${selectedItem}...</div>`;

                // Simulate navigating to the link
                setTimeout(() => {
                    window.location.href = `https://www.example.com/${selectedItem}`;
                }, 1500);
            } else {
                outputElement.innerHTML += `<div class="command-line">${inputText}: command not found</div>`;
            }

            inputField.textContent = '';
            outputElement.scrollTop = outputElement.scrollHeight;
            inputField.focus();
            event.preventDefault();
        }
    });
});

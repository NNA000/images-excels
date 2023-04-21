class ElementManager {
    /*
    Considering element like this
    <div class="contador" id="counter">
            <h2 class="contador-content">
                0
            </h2>
        </div>
    This allow to change content of that element*/

    constructor(elementId) {
        this.element = document.getElementById(elementId);
        this.content_text = this.element.querySelector('.contador-content')
    }

    hide() {
        this.element.style.display = 'none';
    }

    show() {
        this.element.style.display = 'block';
    }
    set_content(text) {
        this.content_text.textContent = text
    }
    set_default_content() {
        this.content_text.textContent = "0"
    }
}

class ClipboardUtils {
    static copyTextToClipboard(text) {
        // Create a temporary input element to hold the text
        const input = document.createElement('input');
        input.setAttribute('value', text);
        document.body.appendChild(input);

        // Select the text in the input element and copy it to the clipboard
        input.select();
        document.execCommand('copy');

        // Remove the temporary input element
        document.body.removeChild(input);
    }
}

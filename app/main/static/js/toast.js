class ToastManager {
    constructor(toastid='general-toast', config={ autohide: true, delay: 1400}) {
      // Initialize the toast element
      this.$toast = $(`#${toastid}`).toast(config);
    }

    // Method to show a toast notification
    show(message) {
      // closing if there is another one
      this.hide()
      // Update the text of the toast element
      this.$toast.find('.toast-body').text(message);
      // Show the toast element
      this.$toast.toast('show');
    }
    // Method to hide the toast notification
    hide() {
      // Hide the toast element
      this.$toast.toast('hide');
    }
  }
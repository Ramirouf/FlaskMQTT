/* static/js/main.js */

document.addEventListener("DOMContentLoaded", function () {
  // Get elements from the DOM
  const nodeSelector = document.getElementById("node-selector");
  const setpointInput = document.getElementById("setpoint-value");
  const blinkButton = document.getElementById("blink-button");
  const setpointButton = document.getElementById("setpoint-button");
  const statusMessage = document.getElementById("status-message");

  // The container div holds the API URLs in its data attributes
  const controlsContainer = document.getElementById("mqtt-controls");
  const blinkUrl = controlsContainer.dataset.blinkUrl;
  const setpointUrl = controlsContainer.dataset.setpointUrl;

  /**
   * Shows a status message using Bootstrap's alert component.
   * @param {string} message The message to display.
   * @param {boolean} isError True for an error (red), false for success (green).
   */
  function showStatus(message, isError = false) {
    // Clear previous state
    statusMessage.textContent = message;
    statusMessage.classList.remove("d-none", "alert-success", "alert-danger");

    // Set new state
    if (isError) {
      statusMessage.classList.add("alert-danger");
    } else {
      statusMessage.classList.add("alert-success");
    }

    // Hide the message after 4 seconds
    setTimeout(() => {
      statusMessage.classList.add("d-none");
    }, 4000);
  }

  /**
   * A generic function to POST data to a URL and handle the response.
   * @param {string} url The URL to send the request to.
   * @param {object} body The JSON body of the request.
   */
  function postData(url, body) {
    fetch(url, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(body),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error(`Server responded with status: ${response.status}`);
        }
        return response.json();
      })
      .then((data) => {
        showStatus(data.message, data.status !== "success");
      })
      .catch((error) => {
        console.error("Fetch Error:", error);
        showStatus("A network or server error occurred. Check the console.", true);
      });
  }

  // Event listener for "Enviar destello" button
  blinkButton.addEventListener("click", () => {
    const nodeId = nodeSelector.value;
    postData(blinkUrl, { node_id: nodeId });
  });

  // Event listener for "Enviar setpoint" button
  setpointButton.addEventListener("click", () => {
    const nodeId = nodeSelector.value;
    const setpointValue = setpointInput.value;
    postData(setpointUrl, { node_id: nodeId, setpoint: setpointValue });
  });
});

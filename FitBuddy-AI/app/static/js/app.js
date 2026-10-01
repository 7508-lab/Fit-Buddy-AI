document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll("[data-loading-form]").forEach((form) => {
    form.addEventListener("submit", () => {
      const button = form.querySelector("button[type='submit']");
      if (!button) return;
      button.classList.add("is-loading");
      button.disabled = true;
      button.setAttribute("aria-busy", "true");
    });
  });

  document.querySelectorAll("[data-copy-target]").forEach((button) => {
    button.addEventListener("click", async () => {
      const target = document.getElementById(button.dataset.copyTarget);
      if (!target) return;
      try {
        await navigator.clipboard.writeText(target.innerText);
        const original = button.textContent;
        button.textContent = "Copied";
        setTimeout(() => { button.textContent = original; }, 1600);
      } catch (_) {
        button.textContent = "Select and copy";
      }
    });
  });
});

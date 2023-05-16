function generatePassword(length) {
    const charset = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+~`|}{[]\:;?><,./-=";
    let password = "";
    for (let i = 0; i < length; i++) {
      password += charset.charAt(Math.floor(Math.random() * charset.length));
    }
    return password;
  }
  
  document.getElementById("generate-password").addEventListener("click", () => {
    const length = document.getElementById("length-slider").value;
    const password = generatePassword(length);
    document.getElementById("password").value = password;
  });
  
  document.getElementById("copy-password").addEventListener("click", () => {
    const password = document.getElementById("password").value;
    navigator.clipboard.writeText(password);
  });
  
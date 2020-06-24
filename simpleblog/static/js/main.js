function shuffleTickers() {
    const targetIds = ['ticker-1', 'ticker-2', 'ticker-3'];
    const shuffledIds = targetIds.sort(() => Math.random() - 0.5);
    let replacement = '';
    shuffledIds.forEach((id) => {
        replacement += document.getElementById(id).outerHTML
    });
    document.getElementById('ticker-container').innerHTML = replacement;
}

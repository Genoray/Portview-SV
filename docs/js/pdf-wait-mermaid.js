// Wait for all Mermaid diagrams to render before PDF export
(async () => {
  // Wait for Mermaid to initialize
  const maxWait = 10000;
  const interval = 200;
  let elapsed = 0;

  while (elapsed < maxWait) {
    const pending = document.querySelectorAll('.mermaid:not([data-processed])');
    const rendered = document.querySelectorAll('.mermaid[data-processed] svg, .mermaid svg');

    if (pending.length === 0 && rendered.length > 0) {
      break;
    }

    // Also check if mermaid code blocks have been converted
    const codeBlocks = document.querySelectorAll('pre > code.mermaid');
    if (codeBlocks.length === 0 && rendered.length > 0) {
      break;
    }

    await new Promise(r => setTimeout(r, interval));
    elapsed += interval;
  }

  // Extra settle time for SVG rendering
  await new Promise(r => setTimeout(r, 1000));
})();

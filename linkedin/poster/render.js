// Usage: node linkedin/poster/render.js <spec.json> <out.png>
// spec: {kicker, emoji, title (use *word* for the serif highlight), sub, bullets[3], pills[], url, accent "r,g,b", h1size}
const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [specPath, outPath] = process.argv.slice(2);
  const spec = JSON.parse(fs.readFileSync(specPath, 'utf8'));
  const tpl = fs.readFileSync(path.join(__dirname, 'template.html'), 'utf8')
    .replace('<script>', '<script>window.POSTER=' + JSON.stringify(spec) + ';</script><script>');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  await page.setContent(tpl, { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  // shrink the title until the layout fits the card
  for (let size = spec.h1size || 78; size >= 52; size -= 4) {
    await page.evaluate(s => document.documentElement.style.setProperty('--h1size', s + 'px'), size);
    const overflow = await page.evaluate(() => {
      const c = document.querySelector('.card');
      return c.scrollHeight > c.clientHeight + 1;
    });
    if (!overflow) break;
  }
  await page.screenshot({ path: outPath, type: 'png' });
  await browser.close();
})();

module.exports = {
  content: ["_site/**/*.html", "_site/**/*.js"],
  css: ["_site/assets/css/*.css"],
  output: "_site/assets/css/",
  skippedContentGlobs: ["_site/assets/**/*.html"],
  safelist: {
    // The publication button icons (_sass/_custom.scss) match on link URLs, e.g.
    // a.btn[href^="https://doi.org/"]; PurgeCSS drops those attribute selectors,
    // so keep every rule under .links
    greedy: [/^links$/],
    standard: [
      "collapse",
      "collapsing",
      "show",
      "dropdown-menu",
      "dropdown-item",
      "table",
      "table-dark",
      "table-hover",
      "table-responsive",
      "af-tooltip",
      "af-popover",
      "font-weight-bold",
      "font-weight-medium",
      "font-weight-lighter",
      // medium-zoom injects these at runtime, so they never appear in the static
      // HTML PurgeCSS scans; without them the zoom overlay's z-index rule is purged
      // and page chrome (scroll-progress bar, ToC) bleeds through a zoomed image.
      "medium-zoom-overlay",
      "medium-zoom-image--opened",
    ],
  },
};

export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: { sans: ['Nunito', 'system-ui', 'sans-serif'], mono: ['JetBrains Mono', 'ui-monospace', 'Consolas', 'monospace'] },
      colors: {
        ink: '#1e2447', soft: '#5b628a', canvas: '#eceaff',
        primary: { DEFAULT: '#5b4fd9', dark: '#4a3fc0', light: '#ece9ff' },
        sky: { clay: '#dcecff' }, mint: { DEFAULT: '#2fb98c', light: '#d8f6ea', dark: '#17775a' },
      },
    },
  },
  plugins: [],
};

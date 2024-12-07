import { mdsvex } from 'mdsvex';
import adapter from '@sveltejs/adapter-static';
import { vitePreprocess } from '@sveltejs/vite-plugin-svelte';

/** @type {import('@sveltejs/kit').Config} */
const config = {
    // Consult https://svelte.dev/docs/kit/integrations
    // for more information about preprocessors
    preprocess: [vitePreprocess(), mdsvex()],

    kit: {
        // Configure the static adapter with a custom output directory
        adapter: adapter({
            pages: 'build', // Output directory for built pages
            assets: 'build', // Output directory for built assets
            fallback: null
        })
    },

    extensions: ['.svelte', '.svx']
};

export default config;

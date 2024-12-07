<script lang="ts">
	import { i18n } from '$lib/i18n';
	import { ParaglideJS } from '@inlang/paraglide-sveltekit';
	import Header from './Header.svelte';
	import '../app.css';

	let { children } = $props();
</script>

<ParaglideJS {i18n}>
	<div class="app">
		<Header></Header>

		<main>
			{@render children()}
		</main>

		<footer>
			<a 
				href="https://github.com/JacobKurtzbergsNickname/bird_stack" 
				target="_blank" 
				rel="noopener noreferrer"
				aria-label="Visit the bird_stack GitHub repository">
				🐦 Visit the bird_stack GitHub repository 🐦‍⬛
			</a>
		</footer>
	</div>
</ParaglideJS>

<style>
	@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');
	.app {
		display: flex;
		flex-direction: column;
		min-height: 100vh;
		font-family: "Press Start 2P", sans-serif;
		color: ghostwhite;
		background-color: steelblue;
	}

	main {
		flex: 1;
		display: flex;
		flex-direction: column;
		padding: 1rem;
		width: 100%;
		max-width: 64rem;
		margin: 0 auto;
		box-sizing: border-box;
	}

	footer {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		padding: 12px;
	}

	footer a {
		font-weight: bold;
	}

	@media (min-width: 480px) {
		footer {
			padding: 12px 0;
		}
	}
</style>

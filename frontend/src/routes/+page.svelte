<script lang="ts">
    import { onMount } from 'svelte';
    import { getBirds } from '$lib/api';

    let birds: any[] = [];
    let error: string | null = null;

    onMount(async () => {
        try {
            const data = await getBirds();
            birds = data.birds;
			console.log(birds);
        } catch (err) {
            if (err instanceof Error) {
                error = err.message;
            } else {
                error = String(err);
            }
        }
    });
</script>

<svelte:head>
	<title>Home</title>
	<meta name="description" content="Svelte demo app" />
</svelte:head>

<section>
	<h1>Here be birds</h1>
	<p>🐦</p>

</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
	}
</style>

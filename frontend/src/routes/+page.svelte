<script lang="ts">
    import { onMount } from 'svelte';
    import { getBirds } from '$lib/api';
	import BirdItem from '$lib/components/BirdItem.svelte';

    let birds: any[] = [];
    let error: string | null = null;

    onMount(async () => {
        console.log('Fetching birds');
        try {
            birds = await getBirds();
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
	<h1>🐦 Mythological Birds Galore! 🐦</h1>
    <ul>
        {#each birds as bird}
            <BirdItem bird={bird} />
        {/each}
    </ul>

</section>

<style>
	section {
		display: flex;
		flex-direction: column;
		align-items: center;
		flex: 0.6;
	}

	h1 {
		width: 100%;
        padding-top: 20px;
	}

    ul {
        list-style-type: none;
        padding-top: 20px;
    }
</style>

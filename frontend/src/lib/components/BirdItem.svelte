<script>
  export let bird;
  console.log(bird);
</script>

<article class="bird-card">
  <div class="bird-content">
    <div class="bird-info">
      <h2>{bird.name}</h2>
      <p>Region: {bird.region}</p>
      <p>Countries: {bird.countries.join(', ')}</p>
      <p>Appearances: {bird.appearances.join(', ')}</p>
      {#if bird.other_names}
        <p>Other Names: {bird.other_names.join(', ')}</p>
      {/if}
      {#if bird.similar_entities}
        <p>Similar Entities: {bird.similar_entities.join(', ')}</p>
      {/if}
    </div>
    <div class="bird-image">
      <img src={bird.image} alt={bird.name} />
    </div>
  </div>
</article>

<style>
  .bird-card {
    border: 1px solid #ccc;
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .bird-content {
    display: flex;
    width: 100%;
  }

  .bird-info {
    flex: 2;
  }

  .bird-image {
    flex: 1;
    text-align: right;
  }

  .bird-image img {
    max-width: 100%;
    height: auto;
    border-radius: 0.5rem;
  }

  img {
    width: 500px;
    height: 500px;
  }

  h2 {
    margin-bottom: 0.5rem;
    font-size: 1.5rem;
  }
</style>
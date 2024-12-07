const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

export async function getBirds() {
    const response = await fetch(`${API_BASE_URL}/birds`);
    if (!response.ok) {
        throw new Error(`Failed to fetch birds: ${response.statusText}`);
    }
    return response.json();
}

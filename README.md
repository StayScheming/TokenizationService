# TokenizationService

This is a microservice that is responsible for managing the tokenization process of the generative art. 
It talks to Solana blockchain to execute NFT deployment, manage the NFT availability master list, 
upload NFT token metadata onto token contract via Metaplex's on-chain contract (aka mint), then transfer the NFT to the user in exchange for a minting fee.

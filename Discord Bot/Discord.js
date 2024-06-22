const { Client, GatewayIntentBits, Collection } = require('discord.js');
const { token } = require('./config.json');

const client = new Client({
  intents: [
    GatewayIntentBits.Guilds,
    GatewayIntentBits.GuildMessages,
    GatewayIntentBits.MessageContent,
  ],
});

class VirtualPet {
  constructor(name) {
    this.name = name;
    this.hunger = 50;
    this.happiness = 50;
    this.energy = 50;
  }

  feed() {
    this.hunger -= 20;
    this.happiness += 10;
    this.energy += 10;
    this.checkLimits();
  }

  play() {
    this.hunger += 10;
    this.happiness += 20;
    this.energy -= 20;
    this.checkLimits();
  }

  checkLimits() {
    ['hunger', 'happiness', 'energy'].forEach(attr => {
      this[attr] = Math.max(0, Math.min(this[attr], 100));
    });
  }

  status() {
    return `${this.name}'s status:\nHunger: ${this.hunger}\nHappiness: ${this.happiness}\nEnergy: ${this.energy}`;
  }
}

const pet = new VirtualPet('Buddy');

client.commands = new Collection();

client.once('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
  setInterval(decreaseStats, 30 * 60 * 1000); // Run every 30 minutes
});

client.on('messageCreate', async message => {
  if (!message.content.startsWith('!') || message.author.bot) return;

  const args = message.content.slice(1).trim().split(/ +/);
  const command = args.shift().toLowerCase();

  if (command === 'feed') {
    pet.feed();
    await message.reply(`You fed ${pet.name}! They look satisfied.`);
  } else if (command === 'play') {
    pet.play();
    await message.reply(`You played with ${pet.name}! They seem happier.`);
  } else if (command === 'status') {
    await message.reply(pet.status());
  }else if (command === 'adopt') {
    const petName = args.join(' ');
    if (!petName) return message.reply('Please provide a name for your pet!');

    if (pets.has(message.author.id)) {
        return message.reply(`You already have a pet named ${pets.get(message.author.id).name}!`);
    }

    const newPet = new VirtualPet(petName);
    pets.set(message.author.id, newPet);
    message.reply(`Congratulations! You've adopted ${petName}.`);
}
});

function decreaseStats() {
  pet.hunger += 5;
  pet.happiness -= 5;
  pet.energy -= 5;
  pet.checkLimits();
}

client.login(token);

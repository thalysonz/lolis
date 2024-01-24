import requests
import json
import time

# URL do endpoint GraphQL
url = "https://u.gg/api"

# Cabeçalhos da requisição
headers = {
    "Content-Type": "application/json",
    "X-App-Version": "9418770622d8abe250f172a18210034db79ea18f",
    "X-App-Type": "Web",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
player1 = 0
player2 = 0

# Corpo da requisição
##data about match, by match
def matchDetails(id):
  global player1
  global player2
  matchId = str(id)
  query = {"operationName":"match","variables":{"regionId":"br1","riotUserName":"takarinkashiku2","riotTagLine":"br2","matchId":matchId,"version":"14_1"},"query":"query match($matchId: String!, $regionId: String!, $riotUserName: String!, $riotTagLine: String!, $version: String!) {\n  match(\n    matchId: $matchId\n    regionId: $regionId\n    riotUserName: $riotUserName\n    riotTagLine: $riotTagLine\n    version: $version\n  ) {\n    allPlayerRanks {\n      rankScores {\n        lastUpdatedAt\n        losses\n        lp\n        queueType\n        rank\n        role\n        seasonId\n        tier\n        wins\n        __typename\n      }\n      riotUserName\n      riotTagLine\n      __typename\n    }\n    historicalData {\n      kaDifferenceFrames {\n        oppValue\n        timestamp\n        youValue\n        __typename\n      }\n      xpDifferenceFrames {\n        oppValue\n        timestamp\n        youValue\n        __typename\n      }\n      teamOneOverview {\n        bans\n        baronKills\n        dragonKills\n        gold\n        inhibitorKills\n        kills\n        riftHeraldKills\n        towerKills\n        __typename\n      }\n      teamTwoOverview {\n        bans\n        baronKills\n        dragonKills\n        gold\n        inhibitorKills\n        kills\n        riftHeraldKills\n        towerKills\n        __typename\n      }\n      runes\n      skillPath\n      statShards\n      accountIdV3\n      csDifferenceFrames {\n        oppValue\n        timestamp\n        youValue\n        __typename\n      }\n      finishedItems {\n        itemId\n        timestamp\n        type\n        __typename\n      }\n      goldDifferenceFrames {\n        oppValue\n        timestamp\n        youValue\n        __typename\n      }\n      itemPath {\n        itemId\n        timestamp\n        type\n        __typename\n      }\n      matchId\n      metricsData {\n        cs\n        jungleCs\n        level\n        pid\n        position\n        riotTagLine\n        riotUserName\n        timestamp\n        totalDamageDoneToChampions\n        totalDamageTaken\n        totalGold\n        xp\n        __typename\n      }\n      postGameData {\n        assists\n        augments\n        carryPercentage\n        championId\n        cs\n        damage\n        damageTaken\n        deaths\n        gold\n        items\n        jungleCs\n        keystone\n        kills\n        level\n        role\n        subStyle\n        riotUserName\n        riotTagLine\n        summonerSpells\n        teamId\n        wardsPlaced\n        level\n        __typename\n      }\n      timelineData {\n        assistPids\n        assistRiotIds {\n          username\n          tagLine\n          __typename\n        }\n        buildingType\n        eventType\n        killerId\n        killerIds\n        laneType\n        monsterSubtype\n        monsterType\n        pid\n        position\n        riotTagLine\n        riotUserName\n        teamId\n        timestamp\n        towerType\n        victimId\n        victimRiotTagLine\n        victimRiotUserName\n        wardType\n        __typename\n      }\n      primaryStyle\n      queueType\n      regionId\n      subStyle\n      riotUserName\n      riotTagLine\n      __typename\n    }\n    matchSummary {\n      assists\n      augments\n      championId\n      cs\n      damage\n      deaths\n      gold\n      items\n      jungleCs\n      killParticipation\n      kills\n      level\n      matchCreationTime\n      matchDuration\n      matchId\n      maximumKillStreak\n      primaryStyle\n      queueType\n      regionId\n      role\n      runes\n      subStyle\n      summonerName\n      riotUserName\n      riotTagLine\n      summonerSpells\n      psHardCarry\n      psTeamPlay\n      lpInfo {\n        lp\n        placement\n        promoProgress\n        promoTarget\n        promotedTo {\n          tier\n          rank\n          __typename\n        }\n        __typename\n      }\n      teamA {\n        championId\n        summonerName\n        riotUserName\n        riotTagLine\n        teamId\n        role\n        hardCarry\n        teamplay\n        placement\n        playerSubteamId\n        __typename\n      }\n      teamB {\n        championId\n        summonerName\n        riotUserName\n        riotTagLine\n        teamId\n        role\n        hardCarry\n        teamplay\n        placement\n        playerSubteamId\n        __typename\n      }\n      version\n      visionScore\n      win\n      __typename\n    }\n    playerInfo {\n      accountIdV3\n      accountIdV4\n      exodiaUuid\n      iconId\n      puuidV4\n      regionId\n      summonerIdV3\n      summonerIdV4\n      summonerLevel\n      riotUserName\n      riotTagLine\n      __typename\n    }\n    performanceScore {\n      damageShare\n      damageShareAgg\n      damageShareTotal\n      finalLvlDiff\n      finalLvlDiffAgg\n      finalLvlDiffTotal\n      goldShare\n      goldShareAgg\n      goldShareTotal\n      hardCarry\n      killParticipation\n      killParticipationAgg\n      killParticipationTotal\n      kpOverGs\n      kpOverGsAgg\n      kpOverGsTotal\n      riotUserName\n      riotTagLine\n      teamplay\n      visionScore\n      visionScoreAgg\n      visionScoreTotal\n      __typename\n    }\n    winningTeam\n    __typename\n  }\n}"}

  # Fazendo a requisição POST (não execute esta parte, apenas copie o código)
  response = requests.post(url, headers=headers, json=query)
  data = response.json()

  postgame = data['data']['match']['historicalData']['postGameData']

  username_to_filter = "takarinkashiku2"
  username_to_filter2 = "Magão"
  try:
    filteredPlayer1 = [player for player in postgame if (player["riotUserName"] == username_to_filter or player["riotUserName"] == "putz e a irelia")]

    filteredPlayer2 = [player for player in postgame if player["riotUserName"] == username_to_filter2]

    danoplayer1 = filteredPlayer1[0]["damage"]
    danoplayer2 = filteredPlayer2[0]["damage"]

    carryPlayer1 = round((filteredPlayer1[0]["carryPercentage"]*100),1)
    carryPlayer2 = round((filteredPlayer2[0]["carryPercentage"]*100),1)


    if (danoplayer1 > danoplayer2):
      print("MatchId: ", matchId, username_to_filter, "https://www.leagueofgraphs.com/pt/match/br/"+matchId)
      player1+=1
    elif(danoplayer2 > danoplayer1):
      print("MatchId: ", matchId, username_to_filter2, "https://www.leagueofgraphs.com/pt/match/br/"+matchId)
      player2+=1
    else:
       print("MatchId: ", matchId, "UM TERCEIRO DEU MAIS DANO", "https://www.leagueofgraphs.com/pt/match/br/"+matchId)
  except:
    print("ISSUE", "https://www.leagueofgraphs.com/pt/match/br/"+matchId)




page = 2

query = {"operationName":"FetchMatchSummaries","variables":{"regionId":"br1","riotUserName":"takarinkashiku2","riotTagLine":"br2","queueType":[440],"duoRiotUserName":"","duoRiotTagLine":"","role":[],"seasonIds":[22,21],"championId":[],"page":page},"query":"query FetchMatchSummaries($championId: [Int], $page: Int, $queueType: [Int], $duoRiotUserName: String, $duoRiotTagLine: String, $regionId: String!, $role: [Int], $seasonIds: [Int]!, $riotUserName: String!, $riotTagLine: String!) {\n  fetchPlayerMatchSummaries(\n    championId: $championId\n    page: $page\n    queueType: $queueType\n    duoRiotUserName: $duoRiotUserName\n    duoRiotTagLine: $duoRiotTagLine\n    regionId: $regionId\n    role: $role\n    seasonIds: $seasonIds\n    riotUserName: $riotUserName\n    riotTagLine: $riotTagLine\n  ) {\n    finishedMatchSummaries\n    totalNumMatches\n    matchSummaries {\n      assists\n      augments\n      championId\n      cs\n      damage\n      deaths\n      gold\n      items\n      jungleCs\n      killParticipation\n      kills\n      level\n      matchCreationTime\n      matchDuration\n      matchId\n      maximumKillStreak\n      primaryStyle\n      queueType\n      regionId\n      role\n      runes\n      subStyle\n      summonerName\n      riotUserName\n      riotTagLine\n      summonerSpells\n      psHardCarry\n      psTeamPlay\n      lpInfo {\n        lp\n        placement\n        promoProgress\n        promoTarget\n        promotedTo {\n          tier\n          rank\n          __typename\n        }\n        __typename\n      }\n      teamA {\n        championId\n        summonerName\n        riotUserName\n        riotTagLine\n        teamId\n        role\n        hardCarry\n        teamplay\n        placement\n        playerSubteamId\n        __typename\n      }\n      teamB {\n        championId\n        summonerName\n        riotUserName\n        riotTagLine\n        teamId\n        role\n        hardCarry\n        teamplay\n        placement\n        playerSubteamId\n        __typename\n      }\n      version\n      visionScore\n      win\n      __typename\n    }\n    __typename\n  }\n}"}

response = requests.post(url, headers=headers, json=query)
data = response.json()

for x in range(0,20):
  mId = data["data"]["fetchPlayerMatchSummaries"]["matchSummaries"][x]["matchId"]
  matchDetails(mId)
  #time.sleep(1)

print("\n\t")
print("Pagina: ", page)
print("Takarinkashiku2 deu mais dano em ", player1, " jogos")
print("Magao deu mais dano em ", player2, " jogos")
  #print("Num: ",x,"matchId: ",data["data"]["fetchPlayerMatchSummaries"]["matchSummaries"][x]["matchId"])



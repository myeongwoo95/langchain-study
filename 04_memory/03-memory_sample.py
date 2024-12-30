from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory(
  return_messages=True, # Chat models에 쉽게 전달할 수 있는 형식으로 출력
)

memory.save_context(
  {
    "input": "안녕하세요!",
  },
  {
    "output": "안녕하세요! 만나서 반가워요.",
  }
)

memory.save_context(
  {
    "input": "오늘 날씨가 좋네요",
  },
  {
    "output": "저는 AI이기 때문에 실제 날씨를 느낄 수는 없지만, 날씨가 좋은 날은 외출이나 활동을 즐기기에 좋은 날입니다!",
  }
)

print(memory.load_memory_variables({}))


from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers.generation import GenerationConfig

# Note: The default behavior now has injection attack prevention off.
tokenizer = AutoTokenizer.from_pretrained("./Qwen-1_8B-Chat", trust_remote_code=True)

# use bf16
# model = AutoModelForCausalLM.from_pretrained("./Qwen-1_8B-Chat", device_map="auto", trust_remote_code=True, bf16=True).eval()

# use fp16
# model = AutoModelForCausalLM.from_pretrained("./Qwen-1_8B-Chat", device_map="auto", trust_remote_code=True, fp16=True).eval()

# use cpu only
# model = AutoModelForCausalLM.from_pretrained("./Qwen-1_8B-Chat", device_map="cpu", trust_remote_code=True).eval()

# use auto mode, automatically select precision based on the device.
model = AutoModelForCausalLM.from_pretrained("./Qwen-1_8B-Chat", device_map="auto", trust_remote_code=True).eval()

# Specify hyperparameters for generation. But if you use transformers>=4.32.0, there is no need to do this.
# model.generation_config = GenerationConfig.from_pretrained("./Qwen-1_8B-Chat", trust_remote_code=True) # 可指定不同的生成长度、top_p等相关超参
'''
# 第一轮对话 1st dialogue turn
response, history = model.chat(tokenizer, "你好", history=None)
print(response)


# 第二轮对话 2nd dialogue turn
response, history = model.chat(tokenizer, "给我讲一个年轻人奋斗创业最终取得成功的故事。", history=history)
print(response)
'''
# Qwen-1.8B-Chat现在可以通过调整系统指令（System Prompt），实现角色扮演，语言风格迁移，任务设定，行为设定等能力。
# Qwen-1.8B-Chat can realize roly playing, language style transfer, task setting, and behavior setting by system prompt.
response, _ = model.chat(tokenizer, "你好呀", history=None, system="请用二次元可爱语气和我说话")
print(response)

